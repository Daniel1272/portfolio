import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from preprocessing import X, y


np.random.seed(0)
# Split dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# Set max depth for weak learners (decision trees)
max_deep = 1
# Number of boosting rounds
T = 100

# Lists to hold trained models and their corresponding weights (alphas)
algs = []
algs_alpha = []

# Initialize uniform sample weights
w = np.ones(len(y_train)) / len(y_train)

# AdaBoost training loop
for t in range(T):

    # Train a weak learner with sample weights
    model = DecisionTreeClassifier(criterion='gini', max_depth=max_deep)
    model.fit(x_train, y_train, sample_weight=w)
    algs.append(model)

    # Predict on training data
    y_pred = model.predict(x_train)

    # Compute weighted error
    err = np.sum(w * (y_train != y_pred))
    # Avoid division by zero
    err = max(err, 1e-10)

    # Compute alpha (model weight) based on error
    alpha = 0.5 * np.log((1 - err) / err)
    algs_alpha.append(alpha)

    # Update sample weights: increase weights of misclassified samples
    M = alpha*y_train*y_pred
    w = w * np.exp(-M)
    # Normalize weights
    w = w/w.sum()

# Make predictions on the test set by summing weighted votes
all_preds = np.array([alpha * alg.predict(x_test) for alg, alpha in zip(algs, algs_alpha)])
final_pred = np.sign(np.sum(all_preds, axis=0))

# Calculate accuracy on test data
ada_score = accuracy_score(y_test, final_pred)
