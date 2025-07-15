import numpy as np
import xgboost as xgb
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score
from preprocessing import X, y  # твои данные

np.random.seed(0)
y = np.where(y==-1,0,1)


x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

"""
xgb_clf = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=0)

params = {
    'n_estimators': [50, 100, 150],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.7, 1],
    'colsample_bytree': [0.7, 1]
}

grid = GridSearchCV(estimator=xgb_clf, param_grid=params, scoring='accuracy', cv=5, verbose=2, n_jobs=-1)
grid.fit(x_train, y_train)

print("Лучшие параметры:", grid.best_params_)

y_pred = grid.best_estimator_.predict(x_test)
print("Accuracy на тесте:", accuracy_score(y_test, y_pred))
"""
xgb_clf = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss',colsample_bytree = 0.7,
                            learning_rate = 0.2, max_depth = 7, n_estimators = 50, subsample = 1)
xgb_clf.fit(x_train,y_train)
y_pred = xgb_clf.predict(x_test)
xgb_score =  accuracy_score(y_test, y_pred)
