import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from preprocessing import X,y

np.random.seed(0)


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

x_train,x_test,y_train,y_test = train_test_split(X_scaled,y,test_size=0.3)


params = {'C': [0.1, 1,5, 10], 'gamma': ['scale',0.1, 0.01],'kernel': ['linear', 'rbf', 'poly','sigmoid']}
svc = SVC(kernel='rbf')
clf = GridSearchCV(svc, params, cv=5)
clf.fit(x_train, y_train)

SVM_model = clf.best_estimator_
SVM_score = clf.best_score_




