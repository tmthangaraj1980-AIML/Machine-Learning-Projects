import streamlit as st
import joblib
import numpy as np

# Load core pipeline files
try:
    model = joblib.load("random_forest_model.pkl")
    scaler = joblib.load("scaler.pkl")
except Exception as e:
    st.error(f"Error loading pipeline artifacts. Ensure you ran 'churn_model.py' first! Details: {e}")

st.set_page_config(page_title="Churn Optimization Dashboard", layout="centered")

st.title("📊 SaaS Customer Churn Optimizer")
st.write("Production Inference Engine for Customer Risk Mitigation Scoring.")
st.markdown("---")

st.sidebar.header("Customer Profile Metrics")
age = st.sidebar.slider("Customer Age", 18, 80, 35)
tenure = st.sidebar.slider("Tenure Profile (Months)", 0, 72, 24)
monthly = st.sidebar.number_input("Monthly Subscription Charge ($)", 20.0, 150.0, 65.0)

# Categorical mapping dropdown
sub_type = st.sidebar.selectbox("Subscription Tier", ["Basic", "Standard", "Premium"])
sub_mapping = {"Basic": 0.0, "Standard": 1.0, "Premium": 2.0}
sub_encoded = sub_mapping[sub_type]

tickets = st.sidebar.number_input("Support Tickets (Last 3 Mos)", 0, 20, 2)
last_login = st.sidebar.number_input("Inactivity Window (Days)", 0, 31, 4)

if st.button("Run Risk Assessment Model"):
    # Group inputs matching model pipeline schema
    raw_features = np.array([[age, tenure, monthly, sub_encoded, tickets, last_login]])
    
    # Standardize input numeric scales
    scaled_features = scaler.transform(raw_features)
    
    # Pull probability vectors
    risk_proba = model.predict_proba(scaled_features)[0][1]
    
    st.markdown("### Operational Risk Assessment Report")
    st.metric("Calculated Churn Probability", f"{risk_proba * 100:.1f}%")
    
    if risk_proba >= 0.70:
        st.error("🔴 **CRITICAL RISK CLASS:** Profile exhibits immediate churn signs. Route immediately to Customer Success Retention Queue.")
    elif risk_proba >= 0.40:
        st.warning("🟡 **ELEVATED RISK CLASS:** Account engagement pattern softening. Target with automated content email workflows.")
    else:
        st.success("🟢 **STABLE CLASS:** Retaining healthy user interaction score profiles.")