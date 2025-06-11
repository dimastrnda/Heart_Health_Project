import streamlit as st
import pickle
import pandas as pd

# Load model dan data referensi
with open('pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)

with open('df.pkl', 'rb') as f:
    df = pickle.load(f)

st.title("Heart Disease Predictor")
st.markdown("Masukkan informasi kesehatanmu untuk melihat apakah kamu berisiko terkena penyakit jantung.")

# Input fields
Age = st.number_input('Age of Person', min_value=1, max_value=120, step=1)
Sex = st.selectbox('Sex', df['Sex'].unique())
ChestPainType = st.selectbox('Chest Pain Type', df['ChestPainType'].unique())
RestingBP = st.number_input('Resting Blood Pressure', min_value=0)
Cholesterol = st.number_input('Serum Cholesterol', min_value=0)
FastingBS = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])
RestingECG = st.selectbox('Resting ECG Results', df['RestingECG'].unique())
MaxHR = st.number_input('Maximum Heart Rate Achieved', min_value=0)
ExerciseAngina = st.selectbox('Exercise-induced Angina', df['ExerciseAngina'].unique())
Oldpeak = st.number_input('ST Depression', format="%.2f")
ST_Slope = st.selectbox('Slope of the Peak Exercise ST Segment', df['ST_Slope'].unique())

# Prediction
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
        'ST_Slope': [ST_Slope]
    })

    result = pipe.predict(input_data)[0]
    st.subheader("Hasil Prediksi:")
    if result == 1:
        st.error("Anda berisiko mengalami penyakit jantung.")
    else:
        st.success("Anda tidak berisiko mengalami penyakit jantung.")
