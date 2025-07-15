Titanic Survival Prediction Ensemble

This project implements an ensemble machine learning pipeline for the Titanic dataset. It combines several models (AdaBoost, SVM, Parzen windows, Bagging, Gradient Boosting, KNN, Gaussian, XGBoost) into a weighted voting ensemble to predict passenger survival.

Project Structure

preprocessing.py – Data cleaning and feature engineering
titanic_adaboost_dinamic.py – AdaBoost model components
titanic_SVM.py – Support Vector Machine model and scaler
parzen_windows.py – Parzen window density estimation
begging.py – Bagging model implementation
titanic_gradient_boost.py – Gradient Boosting trees
titanic_KNN.py – K-Nearest Neighbors model
gaussian.py – Gaussian model
xgboost_titanic.py – XGBoost classifier
meta_model.py – Meta-model (stacking) using Logistic Regression or XGBoost
final_test.py – Script for training meta-model and making predictions on test data
Requirements

Python 3.8+
numpy
pandas
scikit-learn
xgboost
Install dependencies with:

pip install -r requirements.txt
How to Run

Prepare your dataset files (train.csv, test.csv) in the project directory.
Run preprocessing and model training scripts.
Use final_test.py to generate predictions for the test set.
Output CSV file submission8.csv will contain predictions in the required format.
Results

Weighted ensemble achieves approximately 78% accuracy on the Titanic test dataset.
Attempts at stacking with meta-models have been explored but did not significantly improve accuracy.
Notes

Feature engineering includes handling missing values, encoding categorical variables, and feature scaling.
Ensemble weights are tuned manually based on model performance.
Further improvements could be made by hyperparameter tuning and feature selection.