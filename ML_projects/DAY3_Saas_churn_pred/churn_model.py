import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
import joblib

# ==========================================
# 1. DATASET CREATION (STEPS 1, 2 & 3)
# ==========================================
print("⚡ Generating and preprocessing dataset...")
np.random.seed(42)
n_samples = 10000

data = {
    'CustomerID': [f"CUST-{i}" for i in range(n_samples)],
    'Age': np.random.randint(18, 70, size=n_samples),
    'Tenure_Months': np.random.randint(0, 72, size=n_samples),
    'Monthly_Charges': np.random.uniform(20, 120, size=n_samples),
    'Subscription_Type': np.random.choice(['Basic', 'Standard', 'Premium'], size=n_samples, p=[0.5, 0.3, 0.2]),
    'Support_Tickets_Opened': np.random.poisson(lam=1.5, size=n_samples),
    'Last_Login_Days_Ago': np.random.randint(0, 30, size=n_samples),
    'Churn': np.random.choice([0, 1], size=n_samples, p=[0.8, 0.2])
}

df = pd.DataFrame(data)

# Inject correlation signals for the models to learn
df.loc[df['Support_Tickets_Opened'] > 4, 'Churn'] = np.random.choice([0, 1], size=len(df[df['Support_Tickets_Opened'] > 4]), p=[0.2, 0.8])
df.loc[df['Last_Login_Days_Ago'] > 22, 'Churn'] = np.random.choice([0, 1], size=len(df[df['Last_Login_Days_Ago'] > 22]), p=[0.3, 0.7])

# Separate target and drop uninformative key
X = df.drop(columns=['CustomerID', 'Churn'])
y = df['Churn']

# Uniform categorical formatting
X['Subscription_Type'] = X['Subscription_Type'].str.lower().str.strip()

# Ordinal Encoding 
encoder = OrdinalEncoder(categories=[['basic', 'standard', 'premium']])
X['Subscription_Type'] = encoder.fit_transform(X[['Subscription_Type']])

# ==========================================
# 2. STRATIFIED SPLIT, SCALING, SMOTE (STEPS 5 & 6)
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Apply SMOTE strictly to the training data to isolate the test set
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train_scaled, y_train)

# ==========================================
# 3. MODEL BUILDING & EVALUATION (STEPS 7 & 8)
# ==========================================
# Logistic Regression Baseline
lr = LogisticRegression(random_state=42)
lr.fit(X_train_res, y_train_res)
lr_preds = lr.predict(X_test_scaled)

# Random Forest Champion
rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
rf.fit(X_train_res, y_train_res)
rf_preds = rf.predict(X_test_scaled)

print("\n" + "="*40)
print("🏆 BASELINE LOGISTIC REGRESSION PERFORMANCE")
print("="*40)
print(classification_report(y_test, lr_preds))

print("\n" + "="*40)
print("🏆 CHAMPION RANDOM FOREST PERFORMANCE")
print("="*40)
print(classification_report(y_test, rf_preds))
print("Confusion Matrix:")
print(confusion_matrix(y_test, rf_preds))

# ==========================================
# 4. FEATURE IMPORTANCE (STEP 10)
# ==========================================
print("\n" + "="*40)
print("🎯 FEATURE IMPORTANCE WEIGHTS (RANDOM FOREST)")
print("="*40)
importances = rf.feature_importances_
for col, imp in zip(X.columns, importances):
    print(f"{col:<25} : {imp:.4f}")

# Save runtime artifacts for the Streamlit App
joblib.dump(rf, 'random_forest_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("\n✅ Production model assets 'random_forest_model.pkl' and 'scaler.pkl' saved successfully!")