import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from preprocessing import X,y



np.random.seed(0)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


T = 100
F = np.zeros_like(y_train)
trees = []

for i in range(T):

    gradient = (2 * y_train) / (1 + np.exp(2 * y_train * F))


    tree = DecisionTreeRegressor(max_depth=3)
    tree.fit(x_train,gradient)
    predict = tree.predict(x_train)
    trees.append(tree)
    F = F + predict


F_test = np.zeros(len(x_test))
for tree in trees:
    F_test += (tree.predict(x_test))

y_pred = np.sign(F_test)
GD_score = accuracy_score(y_test, y_pred)

