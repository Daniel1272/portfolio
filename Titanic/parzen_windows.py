from sklearn.neighbors import KernelDensity
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
from preprocessing import X,y

np.random.seed(0)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

x_train, x_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=0)

# Разделяем по классам
X_pos = x_train[y_train == 1]
X_neg = x_train[y_train == -1]

# Обучаем KDE (Parzen) для каждого класса
kde_pos = KernelDensity(kernel='epanechnikov', bandwidth=0.5).fit(X_pos)
kde_neg = KernelDensity(kernel='epanechnikov', bandwidth=0.5).fit(X_neg)

# Оцениваем log плотности
log_pos = kde_pos.score_samples(x_test)
log_neg = kde_neg.score_samples(x_test)

# Байесовское правило: сравниваем log-вероятности
y_pred = np.where(log_pos > log_neg, 1, -1)


parzen_score = accuracy_score(y_test, y_pred)