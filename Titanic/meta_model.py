from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score
from titanic_adaboost_dinamic import algs,algs_alpha,ada_score
from titanic_SVM import SVM_model,SVM_score,scaler
from parzen_windows import kde_pos,kde_neg,parzen_score
from begging import begging_model,begging_score
from titanic_gradient_boost import GD_score,trees
from titanic_KNN import KNN_model,KNN_score
from gaussian import gaus_score,gaus_model
from xgboost_titanic import xgb_clf,xgb_score
from preprocessing import X,y


np.random.seed(0)
# Предполагаем, что у тебя уже есть X и y (набор train)
X_base, X_meta, y_base, y_meta = train_test_split(X, y, test_size=0.3)


# Преобразуем X_meta для нужных моделей
X_meta_scaled = scaler.transform(X_meta)

# Собираем признаки для мета-модели
meta_features = np.column_stack([
    np.sign(np.sum([alg.predict(X_meta)*alpha for alg,alpha in zip(algs,algs_alpha)], axis=0)),  # AdaBoost
    SVM_model.predict(X_meta_scaled),                                                           # SVM
    np.where(kde_pos.score_samples(X_meta_scaled) > kde_neg.score_samples(X_meta_scaled), 1, -1),  # Parzen
    begging_model.predict(X_meta),                                                               # Bagging
    np.sign(np.sum([tree.predict(X_meta) for tree in trees], axis=0)),                          # Gradient Boost
    KNN_model.predict(X_meta_scaled),                                                            # KNN
    gaus_model.predict(X_meta_scaled),                                                          # Gaussian
    xgb_clf.predict(X_meta_scaled)
])

# Обучаем мета-модель
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [2, 3, 4],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.8, 1.0],
    'colsample_bytree': [0.8, 1.0]
}

xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)

grid_search = GridSearchCV(
    estimator=xgb,
    param_grid=param_grid,
    scoring='accuracy',  # или 'roc_auc', 'f1' если хочешь
    cv=5,
    verbose=1,
    n_jobs=-1
)

grid_search.fit(meta_features, np.where(y_meta==-1,0,1))

print("Best params:", grid_search.best_params_)
print("Best accuracy:", grid_search.best_score_)

# Используем лучшую модель
meta_model = grid_search.best_estimator_



