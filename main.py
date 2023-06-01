import streamlit as st
import pickle

loadmodel = pickle.load(open('C:/Users/Mhizfair/Desktop/Streamlit Project/Data/Diabetes_model', 'rb'))

def main():
    st.title('Diabetes Prediction')

    # Introduction to Diabetes
    st.markdown("Diabetes is a chronic condition that affects the body's ability to regulate blood sugar levels. Early detection of diabetes is crucial for effective management and prevention of complications.")

    # Definitions and Healthy Ranges
    st.markdown("Please enter the following information for diabetes prediction:")
    st.markdown("**Age**: Age of the individual.")
    st.markdown("**Hypertension**: Whether the individual has hypertension (1 for yes, 0 for no).")
    st.markdown("**Heart Disease**: Whether the individual has heart disease (1 for yes, 0 for no).")
    st.markdown("**BMI**: Body Mass Index of the individual.")
    st.markdown("Healthy BMI range: 18.5 - 24.9")
    st.markdown("**HbA1c Level**: HbA1c level of the individual.")
    st.markdown("Healthy HbA1c range: 4.0 - 5.6")
    st.markdown("**Blood Glucose Level**: Fasting blood glucose level of the individual.")
    st.markdown("Healthy blood glucose range: 70 - 100 mg/dL")

    # Input Variables
    age = st.text_input('Age')
    hypertension = st.selectbox('Hypertension', [0, 1])
    heart_disease = st.selectbox('Heart Disease', [0, 1])
    bmi = st.text_input('BMI')
    hbA1c_level = st.text_input('HbA1c Level')
    blood_glucose_level = st.text_input('Blood Glucose Level')

    # Prediction Code
    if st.button('Predict'):
        make_prediction = loadmodel.predict([[age, hypertension, heart_disease, bmi, hbA1c_level, blood_glucose_level]])
        output = make_prediction[0]
        if output == 1:
            st.write("Diabetic")
            st.write("This prediction is for informational purposes only and should not replace professional medical advice.")
            st.write("Further tests and consultations with a healthcare professional are advised.")
        else:
            st.write("Non-Diabetic")
            

if __name__ == '__main__':
    main()
