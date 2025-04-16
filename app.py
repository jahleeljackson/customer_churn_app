import streamlit as st
import joblib
import numpy as np


scaler = joblib.load('scaler.pkl')
model = joblib.load('model.pkl')


st.title('Customer Churn Prediction App')

st.divider()

st.write('Please enter the appropriate information for a particular customer. Then press predict to receive your prediction.')

st.divider()

age = st.number_input('Enter the age:', min_value = 10, max_value = 100, value = 30)

tenure = st.number_input('Enter the tenure:', min_value = 0, max_value = 130, value = 10)

monthlycharge = st.number_input('Enter the monthly charge:', min_value = 30, max_value = 150)

totalcharge = st.number_input('Enter the total charge:', min_value = 0, max_value = 15000)

contracttype = st.selectbox('Enter the contract type:', ['Month-to-Month', 'One-Year', 'Two-Year'])

gender = st.selectbox('Enter the gender:', ['Male', 'Female'])

st.divider()

predictbutton = st.button('Predict')

st.divider()

if predictbutton :
    gender_selected = 1 if gender == 'Male' else 0
    
    month2month = 1 if contracttype == 'Month-to-Month' else 0
    oneyear = 1 if contracttype == 'One-Year' else 0 
    twoyear = 1 if contracttype == 'Two-Year' else 0

    X = [age, gender_selected, tenure, monthlycharge, totalcharge, month2month, oneyear, twoyear]
    X1 = np.array(X)

    X_array = scaler.transform([X1])

    prediction = model.predict(X_array)[0]

    predicted = 'Does Churn' if prediction == 1 else 'Does Not Churn'

    st.write('Prediction: {}'.format(predicted))
    

else:

    st.write('Please enter values and press \'Predict!\'.')


