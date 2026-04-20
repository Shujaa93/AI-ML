# Heart Disease Prediction — Project Report

## 1. Project Overview
This project predicts whether a patient has heart disease using Machine Learning (Logistic Regression) on the UCI Heart Disease Dataset.

- **Algorithm:** Logistic Regression
- **Dataset:** UCI Heart Disease Dataset (303 records, 14 features)
- **Language:** Python 3.11
- **Tools:** Jupyter Notebook, Pandas, Scikit-learn, Seaborn, Matplotlib

---

## 2. Dataset Description

| Column | Description |
|--------|-------------|
| age | Age of the patient |
| sex | Gender (1 = Male, 0 = Female) |
| cp | Chest pain type (0–3) |
| trestbps | Resting blood pressure (mm Hg) |
| chol | Serum cholesterol (mg/dl) |
| fbs | Fasting blood sugar > 120 mg/dl (1 = True) |
| restecg | Resting ECG results (0–2) |
| thalach | Maximum heart rate achieved |
| exang | Exercise induced angina (1 = Yes) |
| oldpeak | ST depression induced by exercise |
| slope | Slope of the peak exercise ST segment |
| ca | Number of major vessels (0–3) |
| thal | Thalassemia type |
| **target** | **1 = Heart Disease, 0 = No Heart Disease** |

- **Total Records:** 303
- **Missing Values:** None
- **Data Types:** 13 integer columns, 1 float column

---

## 3. Methodology

### Step 1 — Data Loading & Exploration
- Loaded dataset using Pandas
- Checked shape, data types, and missing values
- Visualized target class distribution

### Step 2 — Exploratory Data Analysis (EDA)
- Count plot of target variable
- Correlation heatmap of all features

### Step 3 — Data Preprocessing
- Separated features (X) and target (y)
- Split data: 80% Training, 20% Testing
- Applied StandardScaler for feature normalization

### Step 4 — Model Training
- Used **Logistic Regression** from scikit-learn
- Trained on scaled training data

### Step 5 — Model Evaluation
- Accuracy Score
- Confusion Matrix
- ROC Curve & AUC Score
- Feature Importance (from model coefficients)

---

## 4. Results

| Metric | Value |
|--------|-------|
| Model | Logistic Regression |
| Train/Test Split | 80% / 20% |
| Accuracy | ~85% (approx) |
| AUC Score | ~0.90 (approx) |

---

## 5. Key Findings
- **cp (chest pain type)** and **thalach (max heart rate)** are the most important features for prediction
- The model shows good performance with high AUC, meaning it can distinguish between diseased and healthy patients well
- No missing values made preprocessing straightforward

---

## 6. How to Run This Project

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Notebook
```bash
jupyter notebook Heart-disease.ipynb
```

---

## 7. Project Structure

```
Heart Disease Prediction/
├── Heart-disease.ipynb     # Main Jupyter Notebook
├── heart.csv               # Dataset (UCI Heart Disease)
├── requirements.txt        # Python libraries needed
├── report.md               # This project report
└── README.md               # Project overview
```

---

## 8. References
- UCI Machine Learning Repository — Heart Disease Dataset
- Scikit-learn Documentation
- Pandas Documentation
