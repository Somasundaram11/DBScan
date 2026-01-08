import streamlit as st
import pickle
import numpy as np

# Load model
pickle.load(open("model.pkl", "rb"))

st.title("Life Expectancy Prediction App")

female = st.number_input("Sum of Females Life Expectancy", min_value=0.0, format="%.2f")
total = st.number_input("Sum of Life Expectancy (Both Sexes)", min_value=0.0, format="%.2f")

if st.button("Predict"):
    features = np.array([[female, total]])
    result = model.predict(features)[0]
    st.success(f"Predicted Sum of Males Life Expectancy: {result:.2f}")

