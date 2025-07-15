import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from preprocessing import X,y


np.random.seed(0)
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2)


max_deep = 1
T = 100
algs = []
algs_alpha = []
w = np.ones(len(y_train))/len(y_train)


for t in range(T):
    model = DecisionTreeClassifier(criterion='gini', max_depth=max_deep)
    model.fit(x_train,y_train,sample_weight=w)
    algs.append(model)

    y_pred = model.predict(x_train)

    err = np.sum(w * (y_train != y_pred))
    err = max(err, 1e-10)
    alpha = 0.5 * np.log((1 - err) / err)
    algs_alpha.append(alpha)

    M = alpha*y_train*y_pred
    w = w * np.exp(-M)

    w = w/w.sum()

# Предсказания всех моделей на всём x_test сразу
all_preds = np.array([alpha * alg.predict(x_test) for alg, alpha in zip(algs, algs_alpha)])

# Суммируем предсказания всех моделей
final_pred = np.sign(np.sum(all_preds, axis=0))

ada_score = accuracy_score(y_test, final_pred)





