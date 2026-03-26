
import streamlit as st
import pandas as pd
import joblib
import os

st.title("📚 Smart Study Recommender")

st.write("Enter your subject scores and get a recommendation for which subject to focus on.")

model_path = "model/study_model.pkl"

if not os.path.exists(model_path):
    st.warning("Model not found. Please run src/recommender.py first to train the model.")
else:
    model = joblib.load(model_path)

    physics = st.slider("Physics Score", 0, 100, 50)
    chemistry = st.slider("Chemistry Score", 0, 100, 50)
    maths = st.slider("Maths Score", 0, 100, 50)

    if st.button("Get Recommendation"):
        prediction = model.predict([[physics, chemistry, maths]])
        st.success(f"You should focus more on: {prediction[0].capitalize()}")
