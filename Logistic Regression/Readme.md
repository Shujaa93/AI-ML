# Heart Disease Prediction | Machine Learning

A supervised machine learning project that uses Logistic Regression to predict the presence of heart disease based on patient medical attributes.

## Overview

This project explores how machine learning can be applied to healthcare data to identify patterns associated with heart disease. Using the Heart Disease dataset, a Logistic Regression model is trained to classify patients into two categories: presence or absence of heart disease.

The project focuses on the machine learning workflow, from data exploration and preprocessing to model training, evaluation, and understanding the influence of input features.

## Approach

The dataset is explored to understand its structure, feature distribution, and relationships between variables. After separating the target variable from the input features, the data is split into training and testing sets.

StandardScaler is applied to normalize the features before training the Logistic Regression model. The trained model is then evaluated using classification accuracy, a confusion matrix, and ROC-AUC analysis.

Feature coefficients are also visualized to examine how individual features contribute to the model's predictions.

## Dataset

The project uses the Heart Disease dataset containing 303 records and 13 input features.

The dataset includes patient attributes such as age, sex, chest pain type, blood pressure, cholesterol, maximum heart rate, and other clinical measurements.

| Target | Meaning |
|---|---|
| 0 | No Heart Disease |
| 1 | Heart Disease |

## Model & Results

| Component | Details |
|---|---|
| Algorithm | Logistic Regression |
| Learning Type | Supervised Learning |
| Problem Type | Binary Classification |
| Dataset | Heart Disease Dataset |
| Train/Test Split | 80% / 20% |
| Accuracy | ~85% |
| AUC | ~0.91 |

<caption>Results are approximate and may vary depending on the dataset version and execution.</caption>

## Visual Analysis

The project includes visualizations to better understand the data and model performance:

- Target distribution
- Feature correlation heatmap
- Confusion matrix
- ROC curve
- Feature coefficient visualization

Open `Heart-disease.ipynb` to explore and run the project.

## Visualizations

### Target Distribution
![Target Distribution](images/target_distribution.png)

### Correlation Heatmap
![Correlation Heatmap](images/correlation_heatmap.png)

### Confusion Matrix
![Confusion Matrix](images/confusion_matrix.png)

### ROC Curve
![ROC Curve](images/roc_curve.png)

### Feature Coefficients
![Feature Coefficients](images/feature_importance.png)

## Purpose

This project was developed as a learning project to practice supervised machine learning, data preprocessing,
exploratory data analysis, model evaluation, and feature interpretation using Python.
