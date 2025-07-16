from sklearn.neighbors import KernelDensity
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import numpy as np
from preprocessing import X, y

np.random.seed(0)

# Standardize the feature set
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset into training and testing subsets
x_train, x_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=0)

# Separate training data by class
X_pos = x_train[y_train == 1]
X_neg = x_train[y_train == -1]

# Train Kernel Density Estimators (Parzen Windows) for each class
kde_pos = KernelDensity(kernel='epanechnikov', bandwidth=0.5).fit(X_pos)
kde_neg = KernelDensity(kernel='epanechnikov', bandwidth=0.5).fit(X_neg)

# Evaluate log-likelihoods for test samples under each class model
log_pos = kde_pos.score_samples(x_test)
log_neg = kde_neg.score_samples(x_test)

# Apply Bayes rule: classify based on higher log-likelihood
y_pred = np.where(log_pos > log_neg, 1, -1)

# Compute classification accuracy
parzen_score = accuracy_score(y_test, y_pred)
