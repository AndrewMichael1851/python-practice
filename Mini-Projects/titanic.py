import pandas as pd

titanic = pd.read_csv('_data/titanic.csv')

'''
print(titanic.head())
print('Mean Age: ' + str(titanic['Age'].mean()))
print(titanic[['Age', 'Fare']].describe())
print(titanic[['Sex', 'Age', 'Fare']].groupby('Sex').mean())
'''

titanic.pivot(columns='Age', values='Fare').plot()
