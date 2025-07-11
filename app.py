import streamlit as st
import joblib
import pandas as pd

# Load the trained model

model = joblib.load('SleepHealth_model.pkl')


st.title("🛌 Sleep Disorder Prediction App")

# User input form
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=120)
occupation = st.selectbox("Occupation", [
    "Doctor", "Engineer", "Nurse", "Teacher", "Lawyer", "Accountant",
    "Sales Representative", "Software Engineer", "Scientist", "Manager"
])
sleep_duration = st.slider("Sleep Duration (hours)", 0.0, 12.0, step=0.5)
quality_sleep = st.slider("Quality of Sleep (1-10)", 1, 10)
physical_activity = st.slider("Physical Activity Level", 0, 10)
stress_level = st.slider("Stress Level (1-10)", 1, 10)
bmi_cat = st.selectbox("BMI Category", ["Overweight", "Normal", "Obese", "Normal Weight"])
heart_rate = st.number_input("Heart Rate", 40, 150)
daily_steps = st.number_input("Daily Steps", 0, 30000)
upper_bp = st.number_input("Upper BP", 80, 200)
lower_bp = st.number_input("Lower BP", 40, 130)

# Encodings based on LabelEncoder used in your notebook
gender_map = {"Male": 1, "Female": 0}
bmi_map = {"Overweight": 2, "Normal": 1, "Obese": 0, "Normal Weight": 3}
occupation_map = {
    "Doctor": 5, "Engineer": 8, "Nurse": 9, "Teacher": 4, "Lawyer": 1,
    "Accountant": 7, "Sales Representative": 3, "Software Engineer": 0,
    "Scientist": 2, "Manager": 6
}

# When user clicks Predict
if st.button("Predict"):
    data = pd.DataFrame([{
        'Gender': gender_map[gender],
        'Age': age,
        'Occupation': occupation_map[occupation],
        'Sleep Duration': sleep_duration,
        'Quality of Sleep': quality_sleep,
        'Physical Activity Level': physical_activity,
        'Stress Level': stress_level,
        'BMI Category': bmi_map[bmi_cat],
        'Heart Rate': heart_rate,
        'Daily Steps': daily_steps,
        'Upper BP': upper_bp,
        'Lower BP': lower_bp
    }])

    prediction = model.predict(data)[0]
    disorder_map = {
        0: "Insomnia",
        1: "Sleep Apnea"
    }

    st.success(f"🧠 Predicted Sleep Disorder: **{disorder_map.get(prediction, 'Unknown')}**")
    st.info("⚠️ This is a predictive result. Please consult a healthcare professional for a confirmed diagnosis.")

