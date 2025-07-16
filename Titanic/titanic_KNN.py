import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from preprocessing import X, y

np.random.seed(0)

# Scale features for better distance computation in KNN
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset into training and test sets
x_train, x_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3)

# Define the range of k values to search for the best number of neighbors
n = np.arange(3, 25, 1)
params = {'n_neighbors': n}

# Initialize KNN classifier
knn = KNeighborsClassifier()

# Perform grid search with 5-fold cross-validation
clf = GridSearchCV(knn, params, cv=5)
clf.fit(x_train, y_train)

# Use the best found KNN model
KNN_model = clf.best_estimator_

# Predict on the test set
y_pred = KNN_model.predict(x_test)

# Calculate accuracy
KNN_score = accuracy_score(y_test, y_pred)
