import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from preprocessing import X, y


np.random.seed(0)
# Split the data into training and test sets (70% train, 30% test)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


T = 100  # Number of boosting iterations
F = np.zeros_like(y_train)  # Initialize the model output F(x) = 0
trees = []  # Store all trees

for i in range(T):

    # Compute the gradient
    gradient = (2 * y_train) / (1 + np.exp(2 * y_train * F))

    # Fit regression tree to the gradient
    tree = DecisionTreeRegressor(max_depth=3)
    tree.fit(x_train, gradient)

    # Update model prediction
    predict = tree.predict(x_train)
    trees.append(tree)

    # Update F with current tree's prediction
    F = F + predict


# Make predictions on test data
F_test = np.zeros(len(x_test))
for tree in trees:
    F_test += (tree.predict(x_test))

# Convert final prediction to class labels (-1 or 1)
y_pred = np.sign(F_test)

# Calculate accuracy of the gradient boosting model
GD_score = accuracy_score(y_test, y_pred)
