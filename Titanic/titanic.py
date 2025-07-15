import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('train.csv')
np.random.seed(0)


X = df[['Pclass','Age']]
y = df['Survived'].replace(0,-1)
sex = pd.get_dummies(df['Sex'])
X = pd.concat([X,sex],axis=1)

x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

acc = 0
opt_T = 0

for i in range(1,30):
    max_deep = 3
    T = i
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


    predict = []

    for i in range(len(x_test)):
        x = x_test.iloc[i:i+1]
        res = 0
        for alg,alpha in zip(algs,algs_alpha):
            res += alg.predict(x)*alpha

        predict.append(np.sign(res))

    predict = np.array(predict)
    score = accuracy_score(y_test,predict)

    if score>acc:
        acc = score
        opt_T = T

print(opt_T,acc)