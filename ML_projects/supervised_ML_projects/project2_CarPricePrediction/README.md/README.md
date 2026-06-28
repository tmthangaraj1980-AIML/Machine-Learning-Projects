# 🚗 Car Price Prediction using Machine Learning

## 📌 Project Overview

This project focuses on predicting the selling price of used cars using various Machine Learning regression algorithms.

The project includes:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Log Transformation
* Model Comparison
* Hyperparameter Tuning
* Ensemble Learning using Random Forest and XGBoost

The final model achieved strong regression performance using **XGBoost Regressor with Log Transformation**.

---

# 🎯 Problem Statement

The objective of this project is to build a Machine Learning model capable of predicting the selling price of used cars based on features such as:

* Car Name
* Year
* Fuel Type
* Transmission
* Kilometers Driven
* Seller Information

This helps buyers and sellers estimate fair market prices for used vehicles.

---

# 📂 Dataset

Dataset Used:

* CarDekho Used Car Dataset

Dataset contains:

* Car details
* Selling price
* Fuel type
* Transmission type
* Ownership details
* Kilometers driven

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost

---

# 📊 Exploratory Data Analysis (EDA)

Performed:

* Histogram Analysis
* Boxplot Analysis
* Correlation Analysis
* Outlier Detection
* Distribution Analysis

### Key Observation

The target variable (`selling_price`) showed:

* heavy right skewness
* multiple outliers
* luxury vehicle price extremes

---

# ⚙️ Feature Engineering

Performed:

* Removal of unnecessary columns
* Label Encoding
* Log Transformation of target variable

### Log Transformation

```python
df['selling_price'] = np.log1p(df['selling_price'])
```

This significantly improved model performance by:

* reducing skewness
* stabilizing variance
* compressing extreme values

---

# 🤖 Machine Learning Models Used

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. XGBoost Regressor

---

# 📈 Model Comparison

| Algorithm               | R² Score | RMSE  | Performance |
| ----------------------- | -------- | ----- | ----------- |
| Linear Regression       | 0.66     | 0.479 | Moderate    |
| Decision Tree Regressor | 0.72     | 0.438 | Good        |
| Random Forest Regressor | 0.81     | 0.357 | Very Good   |
| XGBoost Regressor       | 0.84     | 0.339 | Best ✅      |

---

# 🏆 Best Model

## XGBoost Regressor with Log Transformation

### Final Performance

* R² Score: **0.84**
* RMSE: **0.339**
* MAE: **0.240**

---

# 📌 Key Learnings

* Log Transformation can dramatically improve regression performance.
* Ensemble learning models outperform traditional regression techniques.
* XGBoost effectively handles non-linear relationships and complex feature interactions.
* Proper preprocessing and target transformation are critical for real-world regression tasks.

---

# 📷 Project Screenshots

Project includes:

* Selling Price Distribution
* Boxplot Analysis
* Feature Importance
* Actual vs Predicted Plot
* Model Comparison

---

# 📁 Project Structure

```text
DAY2_CarPricePrediction/
│
├── dataset/
│   ├── raw_dataset/
│   └── processed_dataset/
│
├── screenshots/
│
├── Car_Price_Prediction.ipynb
├── README.md
└── requirements.txt
```

---

# 🚀 Future Improvements

* Streamlit Deployment
* Hyperparameter Optimization using GridSearchCV
* Cross Validation
* Deployment using Flask/Render
* Advanced Feature Engineering

---

# 👨‍💻 Author

**Thangaraj T**
Machine Learning Enthusiast | AI & ML Learner

---
