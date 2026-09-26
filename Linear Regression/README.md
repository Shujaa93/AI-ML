# House Price Prediction using Multiple Linear Regression

A simple machine learning project that predicts house prices based on **area, number of bedrooms, and age of the house** using Multiple Linear Regression.

## 📌 Overview

This project demonstrates how multiple independent variables can be used together to predict a continuous target variable (price). It's built as a learning project to understand how `scikit-learn`'s `LinearRegression` handles multiple features and how each feature contributes to the final prediction through its coefficient.

## 📂 Dataset

`home_prices_20.csv` — a small dataset of 20 house records with the following columns:

| Column     | Description                  |
|------------|-------------------------------|
| `area`     | Area of the house (sq ft)     |
| `bedrooms` | Number of bedrooms            |
| `age`      | Age of the house (years)      |
| `price`    | Price of the house (PKR)      |

## 🛠️ Tech Stack

- Python
- pandas
- scikit-learn
- matplotlib

## 🚀 How to Run

1. Clone this repository
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. Install dependencies
   ```bash
   pip install pandas scikit-learn matplotlib
   ```

3. Run the script
   ```bash
   python linear_regression_home_prices.py
   ```

## 🧠 How It Works

1. Load the dataset using `pandas`
2. Visualize the relationship between `area` and `price` using a scatter plot
3. Train a `LinearRegression` model using three features: `area`, `bedrooms`, `age`
4. Extract the model's coefficients and intercept
5. Predict prices for new/unseen houses
6. Save predictions to `predictions.csv`

## 📊 Sample Result

```
Coefficients: [  27.08343668  1581.21829194  -518.92898395]
Intercept: 13966.699180811775

Predicted price for 3000 sqft, 4 bedrooms, 5 years old: [98947.23746482]
```

**Interpretation:**
- Every extra sq ft adds ~27 to the price (holding bedrooms & age constant)
- Every extra bedroom adds ~1581 to the price
- Every extra year of age reduces the price by ~519

## 📈 Example Prediction Output

| area | bedrooms | age | predicted_price |
|------|----------|-----|------------------|
| 2500 | 3        | 10  | 81,229.66        |
| 3500 | 5        | 4   | 114,589.10       |
| 4500 | 6        | 2   | 144,291.62       |

## 🔮 Future Improvements

- Add more features (location, bathrooms, garage, etc.)
- Use a larger, real-world dataset
- Compare performance with other regression models (Ridge, Lasso, Random Forest)
- Add train/test split and evaluation metrics (R², RMSE)

## 👤 Author

Built as part of a Machine Learning practice project.

---
⭐ If you found this useful, feel free to star the repo!
