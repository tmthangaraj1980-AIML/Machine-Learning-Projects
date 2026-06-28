# Day 3: SaaS Churn Prediction App

An end-to-end Machine Learning and Data Science solution built to predict customer churn risk for Software-as-a-Service (SaaS) platforms. This project features a fully interactive web application deployed via Streamlit to provide operational risk assessment reporting.

## 📊 Project Overview
Customer retention is critical for subscription-based business models. This project analyzes behavioral and transactional customer data to proactively identify accounts showing signs of softening engagement or immediate churn risk.

### Key Features:
* **Exploratory Data Analysis (EDA):** Preprocessed and engineered features from raw customer profiles.
* **Predictive Modeling:** Trained a Random Forest classifier to output precise churn probability vectors.
* **Feature Engineering:** Implemented scaling, encoding for subscription types, and handled numeric scale variances.
* **Interactive Dashboard:** Built a Streamlit interface allowing users to input live customer metrics and receive instantaneous risk classifications (Stable, Elevated Risk, Critical Risk).

---

## 🛠️ Tech Stack & Libraries
* **Language:** Python
* **Framework:** Streamlit (UI & Deployment)
* **ML & Data Libraries:** Scikit-Learn, Pandas, NumPy
* **Model Serialization:** Pickle (`.pkl`)

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/tmthangaraj1980-AIML/Machine-Learning-Projects.git](https://github.com/tmthangaraj1980-AIML/Machine-Learning-Projects.git)
   cd Machine-Learning-Projects/ML_projects/DAY3_Saas_churn_pred

   pip install -r requirements.txt

   streamlit run app.py