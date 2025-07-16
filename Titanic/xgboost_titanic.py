import numpy as np
import xgboost as xgb
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score
from preprocessing import X, y

np.random.seed(0)
# Convert labels from -1/1 to 0/1 format required by XGBoost
y = np.where(y == -1, 0, 1)

# Split dataset into training and testing sets (70% train, 30% test)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

"""
# Uncomment to perform hyperparameter tuning with GridSearchCV
xgb_clf = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=0)

params = {
    'n_estimators': [50, 100, 150],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.7, 1],
    'colsample_bytree': [0.7, 1]
}

# Grid search to find the best hyperparameters using 5-fold CV
grid = GridSearchCV(estimator=xgb_clf, param_grid=params, scoring='accuracy', cv=5, verbose=2, n_jobs=-1)
grid.fit(x_train, y_train)

# Evaluate best model on test set
y_pred = grid.best_estimator_.predict(x_test)
print("Accuracy на тесте:", accuracy_score(y_test, y_pred))
"""

# Initialize XGBoost classifier with chosen hyperparameters
xgb_clf = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', colsample_bytree=0.7,
                            learning_rate=0.2, max_depth=7, n_estimators=50, subsample=1)

# Train model on training data
xgb_clf.fit(x_train, y_train)

# Predict labels on test data
y_pred = xgb_clf.predict(x_test)

# Calculate accuracy score on test data
xgb_score = accuracy_score(y_test, y_pred)
