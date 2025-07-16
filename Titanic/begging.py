from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
import numpy as np
from preprocessing import X, y


np.random.seed(0)
# Split dataset into training and testing subsets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
'''
# Define hyperparameter grid for tuning Random Forest
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [4, 6, 8, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2'],
    'bootstrap': [True, False]
}

rf = RandomForestClassifier()

# Perform grid search cross-validation to find best hyperparameters
grid_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=5,
    n_jobs=-1,
    verbose=2
)

grid_search.fit(x_train, y_train)
model = grid_search.best_estimator_'''

# Using best found hyperparameters (or default if grid search is commented out)
model = RandomForestClassifier(bootstrap=False, max_depth=4, max_features='sqrt',
                               min_samples_leaf=1, min_samples_split=10, n_estimators=100)

# Train the Random Forest model
model.fit(x_train, y_train)

# Predict on the test set
y_pred = model.predict(x_test)

# Calculate accuracy score of the model on test data
begging_score = accuracy_score(y_test, y_pred)

# Save the trained model to use later as part of the ensemble
begging_model = model
