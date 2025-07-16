import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from preprocessing import X, y

np.random.seed(0)

# Scale features to have zero mean and unit variance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into train and test sets (70% train, 30% test)
x_train, x_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3)

# Define hyperparameter grid for SVM tuning
params = {'C': [0.1, 1, 5, 10], 'gamma': ['scale', 0.1, 0.01], 'kernel': ['linear', 'rbf', 'poly', 'sigmoid']}

# Initialize SVM model (kernel='rbf' by default)
svc = SVC(kernel='rbf')

# Perform grid search with 5-fold cross-validation
clf = GridSearchCV(svc, params, cv=5)
clf.fit(x_train, y_train)

# Best SVM model found by grid search
SVM_model = clf.best_estimator_
# Best cross-validation accuracy score
SVM_score = clf.best_score_
