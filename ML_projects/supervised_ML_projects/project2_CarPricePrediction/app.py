import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import date
from sklearn.preprocessing import LabelEncoder

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Car Price Prediction App",
    page_icon="🚗",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e3a5f);
    color: white;
}

/* Main titles */
h1, h2, h3 {
    color: white !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #111827);
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* Labels */
label {
    color: white !important;
    font-weight: 600;
}

/* Input boxes */
.stSelectbox div[data-baseweb="select"],
.stNumberInput input,
.stDateInput input {
    background-color: white !important;
    color: black !important;
    border-radius: 10px;
}

/* Dropdown text */
.stSelectbox * {
    color: black !important;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #ec4899, #8b5cf6);
    color: white !important;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #8b5cf6, #06b6d4);
}

/* Success box */
.stAlert {
    background-color: #064e3b !important;
    color: white !important;
    border-radius: 12px;
}

/* Footer */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------
model = pickle.load(open("car_price_model.pkl", "rb"))

# ---------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------
df = pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")

# Remove unwanted columns
df.drop(["seller_type", "owner"], axis=1, inplace=True)

# ---------------------------------------------------
# LABEL ENCODING
# ---------------------------------------------------
le_name = LabelEncoder()
le_fuel = LabelEncoder()
le_transmission = LabelEncoder()

df["name"] = le_name.fit_transform(df["name"])
df["fuel"] = le_fuel.fit_transform(df["fuel"])
df["transmission"] = le_transmission.fit_transform(df["transmission"])

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("👨‍💻 About Developer")

st.sidebar.markdown("""
# Thangaraj T

### ML Engineer | AI Enthusiast

---

## 🚀 Passionate About

- Machine Learning
- AI Applications
- Real-world Data Science
- End-to-End ML Deployment

---

## 📌 Project

Car Price Prediction using XGBoost

---

## ✅ Achievements

- 84% R² Score
- Feature Engineering
- Hyperparameter Tuning
- Log Transformation
- Streamlit Deployment

---

## 🎯 My Goal

To build intelligent AI systems that solve real-world problems and create positive impact through Machine Learning and Data Science.

---

### 🚀 Code. Train. Deploy. Impact.
""")

# ---------------------------------------------------
# MAIN TITLE
# ---------------------------------------------------
st.title("🚗 Car Price Prediction App")

st.markdown("""
## Predict Used Car Selling Prices using Machine Learning

### Built with:
- XGBoost Regressor
- Label Encoding
- Feature Engineering
- Log Transformation
""")

# ---------------------------------------------------
# USER INPUTS
# ---------------------------------------------------
car_name = st.selectbox(
    "🚘 Select Car Name",
    sorted(pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")["name"].unique())
)

purchase_date = st.date_input(
    "📅 Select Car Purchase Date",
    value=date(2018, 1, 1),
    min_value=date(1990, 1, 1),
    max_value=date(2026, 12, 31)
)

year = purchase_date.year

km_driven = st.number_input(
    "🛣️ Kilometers Driven",
    min_value=0,
    max_value=500000,
    value=50000
)

fuel = st.selectbox(
    "⛽ Fuel Type",
    ["Diesel", "Petrol", "CNG", "LPG", "Electric"]
)

transmission = st.selectbox(
    "⚙️ Transmission Type",
    ["Manual", "Automatic"]
)

# ---------------------------------------------------
# ENCODE INPUTS
# ---------------------------------------------------
name_encoded = le_name.transform([car_name])[0]
fuel_encoded = le_fuel.transform([fuel])[0]
transmission_encoded = le_transmission.transform([transmission])[0]

# ---------------------------------------------------
# INPUT DATAFRAME
# ---------------------------------------------------
input_data = pd.DataFrame({
    "name": [name_encoded],
    "year": [year],
    "km_driven": [km_driven],
    "fuel": [fuel_encoded],
    "transmission": [transmission_encoded]
})

# ---------------------------------------------------
# PREDICTION
# ---------------------------------------------------
if st.button("🚀 Predict Car Price"):

    prediction_log = model.predict(input_data)

    predicted_price = np.expm1(prediction_log[0])

    st.success(f"💰 Estimated Selling Price: ₹ {predicted_price:,.0f}")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("""
---
<center>

### 🚀 Developed by Thangaraj T

ML Engineer | AI & Data Science Enthusiast

</center>
""", unsafe_allow_html=True)