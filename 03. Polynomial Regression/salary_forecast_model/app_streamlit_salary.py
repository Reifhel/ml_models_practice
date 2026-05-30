import streamlit as st
import json
import requests

# Title from Aplication
st.title("Salary Forecast Model")

# Inputs
st.write("How many months the employee is with the company?")
months_with_the_company = st.slider(
    "Months", min_value=1, max_value=120, value=60, step=1)

st.write("What is the employee's level  in the company?")
job_level = st.slider("Job Level", min_value=1, max_value=10, value=5, step=1)

# Preparing the data for the API
input_features = {
    "months_with_the_company": months_with_the_company,
    "job_level": job_level
}

# Create a button and handle a event to submit a request on the API
if st.button('Estimate Salary'):
    res = requests.post(url='http://127.0.0.1:8000/predict',
                        json=input_features)

    res_json = json.loads(res.text)
    salary_in_reais = round(res_json['salary_in_reais'], 2)

    st.subheader(f'The estimated salary in reais is R$ {salary_in_reais}')
