import streamlit as st
import pandas as pd
import pickle

# Load model
with open('pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)

# Load data untuk ambil nilai unik
df = pd.read_csv("heart.csv")

st.title("Heart Disease Predictor")

# Input
Age = st.number_input('Age', 1, 120, 30)
Sex = st.selectbox('Sex', df['Sex'].unique())
ChestPainType = st.selectbox('Chest Pain Type', df['ChestPainType'].unique())
RestingBP = st.number_input('RestingBP', 0)
Cholesterol = st.number_input('Cholesterol', 0)
FastingBS = st.selectbox('FastingBS', [0, 1])
RestingECG = st.selectbox('RestingECG', df['RestingECG'].unique())
MaxHR = st.number_input('MaxHR', 0)
ExerciseAngina = st.selectbox('ExerciseAngina', df['ExerciseAngina'].unique())
Oldpeak = st.number_input('Oldpeak', format="%.2f")
ST_Slope = st.selectbox('ST_Slope', df['ST_Slope'].unique())

# Prediksi
if st.button('Predict'):
    input_data = pd.DataFrame({
        'Age': [Age],
        'Sex': [Sex],
        'ChestPainType': [ChestPainType],
        'RestingBP': [RestingBP],
        'Cholesterol': [Cholesterol],
        'FastingBS': [FastingBS],
        'RestingECG': [RestingECG],
        'MaxHR': [MaxHR],
        'ExerciseAngina': [ExerciseAngina],
        'Oldpeak': [Oldpeak],
        'ST_Slope': [ST_Slope],
    })

    result = pipe.predict(input_data)[0]
    st.subheader("Prediction Result:")
    if result == 1:
        st.error("Risiko tinggi penyakit jantung.")
    else:
        st.success("Risiko rendah penyakit jantung.")
