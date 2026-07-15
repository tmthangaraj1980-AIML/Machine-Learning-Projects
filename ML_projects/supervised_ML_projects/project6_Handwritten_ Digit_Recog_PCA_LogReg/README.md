# 🧠 Handwritten Digit Recognition using PCA & Logistic Regression

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Project Overview

This project demonstrates handwritten digit recognition using **Principal Component Analysis (PCA)** for dimensionality reduction and **Logistic Regression** for classification.

The original handwritten digit images contain **784 pixel features (28×28)**. To reduce computational complexity while preserving essential information, PCA is applied to retain **95% of the total variance**, reducing the feature space to **331 principal components**. The transformed data is then classified using Logistic Regression.

This project demonstrates an end-to-end Machine Learning workflow including preprocessing, feature engineering, dimensionality reduction, model training, and evaluation.

---

## 🎯 Objective

- Build a handwritten digit recognition system
- Reduce dimensionality using PCA
- Improve computational efficiency
- Train a Logistic Regression classifier
- Evaluate model performance

---

## 📂 Dataset

**Dataset:** MNIST Handwritten Digits

- 60,000 handwritten digit images
- Image Size: **28 × 28 pixels**
- Original Features: **784**
- Classes: **10 (Digits 0–9)**

---

## 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-Learn
- PCA
- Logistic Regression
- Jupyter Notebook

---

# 🚀 Project Workflow

```
Load Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Scaling
      │
      ▼
Principal Component Analysis (PCA)
      │
      ▼
Train-Test Split
      │
      ▼
Logistic Regression
      │
      ▼
Model Evaluation
      │
      ▼
Prediction
```

---

# 📊 Principal Component Analysis

Original Features

```
784
```

Reduced Features

```
331
```

Variance Retained

```
95%
```

PCA significantly reduces dimensionality while preserving almost all useful information.

---

# 📈 Model Evaluation

Evaluation Metrics

- Accuracy Score
- Confusion Matrix
- Classification Report

Example Evaluation

```
Accuracy : 97%+
```

(The actual accuracy may vary slightly depending on random state.)

---

# 📷 Project Screenshots

## Sample Digits

```
images/sample_digits.png
```

## PCA Explained Variance

```
images/pca_explained_variance.png
```

## Confusion Matrix

```
images/confusion_matrix.png
```

## Prediction Results

```
images/prediction.png
```

---

# 🌍 Real-World Applications

This project demonstrates concepts widely used in:

- OCR (Optical Character Recognition)
- Postal Code Recognition
- Bank Cheque Digit Recognition
- Automated Form Processing
- Document Digitization
- Postal Automation
- Historical Document Recognition

