#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing the datasets
dataset=pd.read_csv('Position_Salaries.csv')
X=dataset.iloc[:, 1:2].values
Y=dataset.iloc[:, 2].values

#Splitting the dataset into Training and Test sets
#from sklearn.model_selection import train_test_split
#X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.2, random_state=0)

#Feature scaling
"""
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)
"""

#Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(X, Y)

#Fitting Polynomial Regression to th dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=5)
X_poly=poly_reg.fit_transform(X)
lin_reg_2=LinearRegression()#Fitting into a Multiple Linear Regression model
lin_reg_2.fit(X_poly, Y)

#Visualizing Linear Regression results
plt.scatter(X, Y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title('Truff or Bluff(Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salaries')
plt.show()

#Visualizing Polynomial Regression results
plt.scatter(X, Y, color='red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
plt.title('Truff or Bluff(Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salaries')
plt.show()

#Predicting the Linear Regression model
lin_reg.predict([[6.5]])

#Predicting the Polynomial Regression model
lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
