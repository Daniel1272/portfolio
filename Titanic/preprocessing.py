import pandas as pd


df = pd.read_csv('train.csv')

y = df['Survived'].replace(0, -1)

# Encode Sex: male=1, female=0
sex = df['Sex'].apply(lambda x: 1 if x == 'male' else 0)

# Fill missing Fare values with median
age = df['Age'].fillna(df['Age'].median())

# Calculate total number of relatives aboard
relatives = df['Parch']+df['SibSp']

# Fill missing Embarked values and create dummy variables
df['Embarked'] = df['Embarked'].fillna('S')
embarked = pd.get_dummies(df['Embarked'])

# Concatenate all features into final feature set
X = pd.concat([df[['Pclass', 'Fare']], sex, age, relatives.rename("Relatives"), embarked], axis=1)
