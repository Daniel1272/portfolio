import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from preprocessing import X,y

np.random.seed(0)


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

x_train,x_test,y_train,y_test = train_test_split(X_scaled,y,test_size=0.3)

n = np.arange(3,25,1)

params = {'n_neighbors':n}

knn = KNeighborsClassifier()

clf = GridSearchCV(knn, params, cv=5)
clf.fit(x_train, y_train)

KNN_model = clf.best_estimator_
y_pred = KNN_model.predict(x_test)
KNN_score = accuracy_score(y_test,y_pred)




