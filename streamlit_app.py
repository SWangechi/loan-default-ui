import streamlit as st
import requests

st.set_page_config(page_title="Loan Default Predictor", page_icon="💰")

st.title("Loan Default Predictor 💳")

st.write("Enter your details below to predict the probability of defaulting on a loan.")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)
income = st.number_input("Annual Income ($)", min_value=1000, value=65000)
loan_amount = st.number_input("Loan Amount ($)", min_value=500, value=20000)
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=720)

if st.button("Predict Default Probability"):
    api_url = "https://loan-default-h43j.onrender.com/predict"  # Your existing API URL
    data = {
        "age": age,
        "income": income,
        "loan_amount": loan_amount,
        "credit_score": credit_score
    }

    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"**Loan Default Probability: {result['loan_default_probability']:.2f}**")
    else:
        st.error("Error: Unable to get prediction. Please try again later.")

