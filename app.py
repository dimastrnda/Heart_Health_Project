import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load pipeline dan fitur
with open('pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)

with open('features.pkl', 'rb') as f:
    feature_columns = pickle.load(f)

with open('df.pkl', 'rb') as f:
    df = pickle.load(f)

st.set_page_config(page_title="Heart Health Prediction", layout="centered")

st.title("🫀 Heart Disease Prediction")
st.markdown("Isi form berikut untuk memprediksi risiko penyakit jantung:")

# Input form
with st.form("heart_form"):
    Age = st.number_input("Age", min_value=1, max_value=120, value=40)
    Sex = st.selectbox("Sex", options=["M", "F"])
    ChestPainType = st.selectbox("Chest Pain Type", options=["ATA", "NAP", "TA", "ASY"])
    RestingBP = st.number_input("Resting Blood Pressure", min_value=50, max_value=250, value=120)
    Cholesterol = st.number_input("Cholesterol", min_value=0, max_value=600, value=200)
    FastingBS = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1])
    RestingECG = st.selectbox("Resting ECG", options=["Normal", "ST", "LVH"])
    MaxHR = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
    ExerciseAngina = st.selectbox("Exercise-induced Angina", options=["Y", "N"])
    Oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    ST_Slope = st.selectbox("ST Slope", options=["Up", "Flat", "Down"])

    submitted = st.form_submit_button("Predict")

# Prediksi
if submitted:
    try:
        input_data = pd.DataFrame([{
            'Age': Age,
            'Sex': Sex,
            'ChestPainType': ChestPainType,
            'RestingBP': RestingBP,
            'Cholesterol': Cholesterol,
            'FastingBS': FastingBS,
            'RestingECG': RestingECG,
            'MaxHR': MaxHR,
            'ExerciseAngina': ExerciseAngina,
            'Oldpeak': Oldpeak,
            'ST_Slope': ST_Slope
        }])

        # Pastikan kolom sesuai urutan saat training
        input_data = input_data[feature_columns]

        # Prediksi
        prediction = pipe.predict(input_data)[0]
        proba = pipe.predict_proba(input_data)[0][1] * 100

        if prediction == 1:
            st.error(f"Hasil prediksi: Berisiko penyakit jantung ({proba:.2f}% kemungkinan)")
        else:
            st.success(f"Hasil prediksi: Tidak berisiko penyakit jantung ({proba:.2f}% kemungkinan)")

    except Exception as e:
        st.exception(f"Terjadi error saat prediksi: {e}")
