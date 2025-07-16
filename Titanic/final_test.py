import pandas as pd
import numpy as np
from titanic_adaboost_dinamic import algs,algs_alpha,ada_score
from titanic_SVM import SVM_model,SVM_score,scaler
from parzen_windows import kde_pos,kde_neg,parzen_score
from begging import begging_model,begging_score
from titanic_gradient_boost import GD_score,trees
from titanic_KNN import KNN_model,KNN_score
from gaussian import gaus_score,gaus_model
from xgboost_titanic import xgb_clf,xgb_score
from meta_model import meta_model

df = pd.read_csv('test.csv')

df['Fare'] = df['Fare'].fillna(df['Fare'].median())
# male == 1, female == 0
sex = df['Sex'].apply(lambda x:1 if x=='male' else 0)

# age fill na
age = df['Age'].fillna(df['Age'].median())
# realatives
relatives = df['Parch']+df['SibSp']

df['Embarked'] = df['Embarked'].fillna('S')
embarked = pd.get_dummies(df['Embarked'])


X = pd.concat([df[['Pclass','Fare']], sex, age, relatives.rename("Relatives"), embarked],axis=1)


#ADABOOST model
res = np.array([(alg.predict(X)*alpha) for alg,alpha in zip(algs,algs_alpha)])
ada_res = np.sign(res.sum(axis=0))*ada_score


#SVM
X_scaled = scaler.transform(X)
res = SVM_model.predict(X_scaled)
SVM_res = res * SVM_score


#PARZEN
# Оцениваем log плотности
log_pos = kde_pos.score_samples(X_scaled)
log_neg = kde_neg.score_samples(X_scaled)

# Байесовское правило: сравниваем log-вероятности
parzen_res = np.where(log_pos > log_neg, 1, -1)*parzen_score

# BEGGING
begging_res = begging_model.predict(X)*begging_score

# Gradient_boost
res = np.array([tree.predict(X) for tree in  trees]).sum(axis=0)
gradient_boost = np.sign(res)*GD_score

# KNN
KNN_res = KNN_model.predict(X_scaled)*KNN_score

# Gaussion
gaus_res = gaus_model.predict(X)*gaus_score

# XGBoost
xgb_res = np.where(xgb_clf.predict(X)==0,-1,1) * xgb_score




"""
total_res = ada_res+SVM_res+parzen_res+begging_res+gradient_boost+KNN_res+gaus_res+xgb_res

total_res = np.sign(total_res)
total_res = np.where(total_res==-1,0,1)
#meta model
"""
meta_features = np.column_stack([np.sign(np.array([(alg.predict(X)*alpha) for alg,alpha in zip(algs,algs_alpha)]).sum(axis=0)),
            SVM_model.predict(X_scaled) ,np.where(log_pos > log_neg, 1, -1) ,
            begging_model.predict(X), np.sign(np.array([tree.predict(X) for tree in  trees]).sum(axis=0)),
            KNN_model.predict(X_scaled), gaus_model.predict(X), np.where(xgb_clf.predict(X)==0,-1,1)])

total_res = meta_model.predict(meta_features)


res = pd.concat([df['PassengerId'],pd.Series(total_res)],axis=1)
res = res.rename(columns={0:'Survived'})

res.to_csv('submission.csv',index=False)

