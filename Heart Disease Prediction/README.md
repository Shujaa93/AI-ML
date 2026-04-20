#  Heart Disease Prediction using Logistic Regression

A machine learning project that predicts the presence of heart disease in patients using clinical features, built with Python and scikit-learn.

---

##  Project Overview

This project applies **Logistic Regression** to the classic Heart Disease dataset to classify whether a patient is likely to have heart disease (1) or not (0). It covers the full ML pipeline: data loading, exploratory data analysis, model training, evaluation, and feature importance visualization.

---

### Steps Explained

1. **Data Loading** — Loads `heart.csv` using pandas with error handling for missing files.
2. **EDA** — Visualizes target class distribution and a correlation heatmap across all features.
3. **Preprocessing** — Drops the target column, splits data (80/20), and applies `StandardScaler`.
4. **Model Training** — Trains a `LogisticRegression` model on the scaled training data.
5. **Evaluation** — Reports accuracy, plots a confusion matrix, and draws the ROC curve with AUC score.
6. **Feature Importance** — Visualizes model coefficients as a horizontal bar chart.

---

##  Results

| Metric | Value |
|--------|-------|
| Accuracy | ~85% (varies by run) |
| AUC Score | ~0.91 |

> Actual results may vary slightly depending on the dataset version used.

### Visualizations Generated

- 📊 **Target Distribution** — Count plot of disease vs. no disease
- 🌡️ **Correlation Heatmap** — Feature correlations across the dataset
- 🔲 **Confusion Matrix** — True/false positives and negatives
- 📈 **ROC Curve** — Model performance across all thresholds
- 📉 **Feature Importance** — Ranked logistic regression coefficients

---

##  Technologies Used

| Library | Purpose |
|--------|---------|
| `pandas` | Data loading and manipulation |
| `numpy` | Numerical operations |
| `matplotlib` | Base plotting |
| `seaborn` | Statistical visualizations |
| `scikit-learn` | ML model, preprocessing, and metrics |

---
