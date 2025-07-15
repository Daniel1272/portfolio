import pandas as pd
import numpy as np


df = pd.read_csv('train.csv')

y = df['Survived'].replace(0,-1)

# male == 1, female == 0
sex = df['Sex'].apply(lambda x:1 if x=='male' else 0)

# age fill na
age = df['Age'].fillna(df['Age'].median())
# realatives
relatives = df['Parch']+df['SibSp']

df['Embarked'] = df['Embarked'].fillna('S')
embarked = pd.get_dummies(df['Embarked'])


X = pd.concat([df[['Pclass','Fare']], sex, age, relatives.rename("Relatives"), embarked],axis=1)





