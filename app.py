import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model.pkl')

st.title("📈 Student Final Exam Score Predictor")

# Inputs
gender = st.selectbox("Gender", ['Male', 'Female'])
study_hours = st.slider("Study Hours per Week", 0, 40)
attendance = st.slider("Attendance Rate (%)", 0, 100)
past_score = st.slider("Past Exam Scores", 0, 100)
parent_edu = st.selectbox("Parental Education", ['High School', 'Bachelor', 'Master', 'PhD'])
internet = st.selectbox("Internet at Home", ['Yes', 'No'])
activities = st.selectbox("Extracurricular Activities", ['Yes', 'No'])

data = {
    'Study_Hours_per_Week': study_hours,
    'Attendance_Rate': attendance,
    'Past_Exam_Scores': past_score,
    'Gender_Male': 1 if gender == 'Male' else 0,
    'Parental_Education_Level_High School': 1 if parent_edu == 'High School' else 0,
    'Parental_Education_Level_Masters': 1 if parent_edu == 'Master' else 0,
    'Parental_Education_Level_PhD': 1 if parent_edu == 'PhD' else 0,
    'Internet_Access_at_Home_Yes': 1 if internet == 'Yes' else 0,
    'Extracurricular_Activities_Yes': 1 if activities == 'Yes' else 0
}


input_df = pd.DataFrame([data])


if st.button("Predict Final Score"):
    result = model.predict(input_df)[0]
    st.success(f"🎯 Predicted Final Exam Score: {result:.2f}")
