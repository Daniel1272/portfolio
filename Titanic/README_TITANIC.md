# 🛳 Titanic: Survival Prediction using Ensemble Learning

This project solves the Titanic Kaggle competition using a wide range of machine learning models combined into a weighted ensemble and a meta-model (stacking). The goal is to predict whether a passenger survived based on features like age, sex, ticket class, etc.

---

## 📦 Project Structure

Titanic/
├── preprocessing.py # Feature engineering and preprocessing
├── titanic_adaboost_dinamic.py # Custom AdaBoost implementation
├── titanic_SVM.py # SVM classifier with scaling
├── parzen_windows.py # Parzen Window classifier (non-parametric density estimation)
├── begging.py # Bagging classifier
├── titanic_gradient_boost.py # Custom Gradient Boosting model
├── titanic_KNN.py # k-Nearest Neighbors model
├── gaussian.py # Gaussian Naive Bayes model
├── xgboost_titanic.py # XGBoost classifier
├── meta_model.py # Meta-model (stacking using XGBoost)
├── submission_generator.py # Generates final Kaggle submission
└── README.md # This file



---

## 📚 Models Used

- ✅ AdaBoost (custom implementation)
- ✅ Support Vector Machine (SVM)
- ✅ Parzen Windows Classifier
- ✅ Bagging
- ✅ Gradient Boosting (from scratch)
- ✅ k-Nearest Neighbors (kNN)
- ✅ Gaussian Naive Bayes
- ✅ XGBoost
- ✅ Meta-model (stacking with XGBoost)

---

## 🧠 Ensemble Strategy

Two ensemble techniques were explored:

### 1. Weighted Voting Ensemble
- Each model prediction is weighted based on cross-validation performance.
- Final prediction is made using a weighted majority vote.
- **Kaggle score:** ~0.78

### 2. Meta-Model (Stacking)
- Model predictions are used as features for an XGBoost meta-classifier.
- After correcting label issues, it achieved similar performance.
- **Kaggle score:** ~0.777

---

## ⚙️ How to Run

1. Install requirements:
pip install -r requirements.txt
2. Run training and create submission:

3. Upload `submission.csv` to [Kaggle Titanic competition](https://www.kaggle.com/c/titanic)

---

## 🔍 Key Learnings

- Ensemble learning significantly improves prediction quality on small tabular datasets.
- Proper label handling is critical when training meta-models (e.g., avoid `-1/1` if model expects `0/1`).
- Custom implementations (AdaBoost, Gradient Boosting) help understand model internals better.

---

## ✅ Result Summary

| Method              | Kaggle Public Score |
|---------------------|---------------------|
| Weighted Ensemble   | 0.78468             |
| Meta-Model (Stack)  | 0.77751             |

---

## 📌 Author

Made by [Daniel Smajorskis](https://github.com/Daniel1272) as part of portfolio projects for junior data analyst / ML roles.


