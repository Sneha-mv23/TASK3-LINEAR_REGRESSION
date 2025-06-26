import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

#  1.Import and preprocess the dataset.
df = pd.read_csv("Housing.csv")
print(df.head())

df = df.dropna()

#feature selection
x = df[['area']]
y = df['price']

#  2.Split data into train-test sets.

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.2,random_state = 42)

#  3.Fit a Linear Regression model using sklearn.linear_model.

model = LinearRegression()
model.fit(x_train,y_train)

#prediction
y_pred = model.predict(x_test)

# 4.Evaluate model using MAE, MSE, R².
print("Mean Absolute Error(MAE): ",mean_absolute_error(y_test,y_pred))
print("Mean squared Error(MSE): ",mean_squared_error(y_test,y_pred))
print("R² Score:", r2_score(y_test, y_pred))

#  5.Plot regression line and interpret coefficients
 
plt.scatter(x_test['area'], y_test, color='blue')
plt.plot(x_test['area'], model.predict(x_test), color='blue')  
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Area vs Price - Linear Regression')
plt.show()

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)  
