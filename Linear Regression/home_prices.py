import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

# Load dataset
##df = pd.read_csv('home-prices.csv')
df = pd.read_csv(r'C:\Users\LENOVO\Desktop\Machine Learning\ML Models\Linear Regression\home-prices.csv')
print(df)

# Visualize area vs price
plt.scatter(df.area, df.price, color='red', marker='+')
plt.xlabel('Area (sq ft)')
plt.ylabel('Price (PKR)')
plt.title('Area vs Price')
plt.show()

# Train multiple linear regression model
reg = linear_model.LinearRegression()
reg.fit(df[['area', 'bedrooms', 'age']], df.price)

print("Coefficients:", reg.coef_)
print("Intercept:", reg.intercept_)

# Predict price for a new house
predicted_price = reg.predict([[3000, 4, 5]])
print("Predicted price for 3000 sqft, 4 bedrooms, 5 years old:", predicted_price)

# Predict for multiple new houses
new_houses = pd.DataFrame({
    'area': [2500, 3500, 4500],
    'bedrooms': [3, 5, 6],
    'age': [10, 4, 2]
})
new_houses['predicted_price'] = reg.predict(new_houses)
print(new_houses)

# Save predictions to csv
new_houses.to_csv('predictions.csv', index=False)
