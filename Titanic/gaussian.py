from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from preprocessing import X,y

np.random.seed(0)


# Split the dataset into training and test sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# QDA
gaus_model = QuadraticDiscriminantAnalysis(reg_param=0.1)
gaus_model.fit(x_train, y_train)

# Predict on the test data
y_pred = gaus_model.predict(x_test)

# Calculate accuracy of the QDA model
gaus_score = accuracy_score(y_test, y_pred)

