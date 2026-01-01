import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

# 1. Setup paths and load models
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, 'models')

try:
    model = joblib.load(os.path.join(model_path, 'xgb_model.pkl'))
    scaler = joblib.load(os.path.join(model_path, 'scaler.pkl'))
    encoder = joblib.load(os.path.join(model_path, 'encoder.pkl'))
    feature_cols = joblib.load(os.path.join(model_path, 'features.pkl'))
except FileNotFoundError as e:
    st.error(f"Set up your 'models' folder correctly! Error: {e}")
    st.stop()

# 2. UI Configuration
st.set_page_config(page_title="Credit Risk AI", layout="centered", page_icon="🏦")
st.title("🏦 Credit Risk Assessment System")
st.markdown("---")

# 3. Input Form
st.subheader("Applicant Information")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Person Age", min_value=18, max_value=100, value=25)
    income = st.number_input("Annual Income", min_value=0, value=50000)
    home_ownership = st.selectbox("Home Ownership", ["RENT", "OWN", "MORTGAGE", "OTHER"])
    emp_length = st.number_input("Years of Employment", min_value=0, max_value=60, value=5)
    intent = st.selectbox("Loan Intent", ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"])

with col2:
    loan_grade = st.selectbox("Loan Grade", ["A", "B", "C", "D", "E", "F", "G"])
    loan_amnt = st.number_input("Loan Amount", min_value=0, value=10000)
    int_rate = st.number_input("Interest Rate (%)", min_value=0.0, value=11.0, step=0.1)
    default_history = st.selectbox("Historical Default?", ["Y", "N"])
    cred_hist = st.number_input("Credit History Length (Years)", min_value=0, value=2)

# Calculation for loan_percent_income (This is the 11th column)
loan_percent_income = loan_amnt / income if income > 0 else 0

st.markdown("---")

# 4. Prediction Logic
if st.button("Analyze Credit Risk", use_container_width=True):
    # Create the DataFrame with exactly 11 columns in the correct order
    # ORDER: age, income, home_ownership, emp_length, intent, grade, amount, rate, percent_income, default, cred_hist
    input_df = pd.DataFrame([[
        age, 
        income, 
        home_ownership, 
        emp_length, 
        intent, 
        loan_grade, 
        loan_amnt, 
        int_rate, 
        loan_percent_income, 
        default_history, 
        cred_hist
    ]], columns=feature_cols)

    # Encode categorical inputs (Home Ownership, Intent, Grade, Default)
    # This uses the names of the columns the encoder was trained on
    try:
        input_df[encoder.feature_names_in_] = encoder.transform(input_df[encoder.feature_names_in_])
        
        # Scale the data
        input_scaled = scaler.transform(input_df)
        
        # Predict
        prediction = model.predict(input_scaled)
        probability = model.predict_proba(input_scaled)[0][1]

        # 5. Display Results
        if prediction[0] == 1:
            st.error(f"### 🚩 Prediction: HIGH RISK")
            st.metric("Probability of Default", f"{probability:.1%}")
            st.warning("Recommendation: Reject or require higher collateral.")
        else:
            st.success(f"### ✅ Prediction: LOW RISK")
            st.metric("Probability of Default", f"{probability:.1%}")
            st.info("Recommendation: Eligible for automated approval.")
            
    except ValueError as e:
        st.error(f"Column Mismatch Error: {e}")
        st.write("Ensure your training columns match the UI input columns.")