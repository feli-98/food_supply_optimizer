import streamlit as st
import pandas as pd
import joblib

st.title("🌾 Food Supply Optimizer")
st.write("Predicting food deficit using simulated supply chain data.")

# Try to load the model with error handling
try:
    model = joblib.load('food_model.joblib')
except FileNotFoundError:
    st.error("❌ Model file not found. Please make sure 'food_model.joblib' is in the repo.")
    st.stop()
except Exception as e:
    st.error(f"⚠️ An unexpected error occurred while loading the model: {e}")
    st.stop()

# Sidebar inputs
st.sidebar.header("📊 Input Features")
surplus = st.sidebar.slider("Surplus", 100, 1000, 500)
distance_km = st.sidebar.slider("Distance (km)", 10.0, 500.0, 100.0)
cost_per_km = st.sidebar.slider("Cost per km", 0.5, 5.0, 2.0)
perishability = st.sidebar.slider("Perishability", 0.1, 1.0, 0.5)
population = st.sidebar.slider("Population", 1000, 100000, 50000)
market_price = st.sidebar.slider("Market Price", 10.0, 100.0, 50.0)

# Prepare input data
input_data = pd.DataFrame({
    'surplus': [surplus],
    'distance_km': [distance_km],
    'cost_per_km': [cost_per_km],
    'perishability': [perishability],
    'population': [population],
    'market_price': [market_price]
})

# Make prediction
try:
    prediction = model.predict(input_data)[0]
    st.subheader(f"📈 Predicted Deficit: {prediction:.2f}")
except Exception as e:
    st.error(f"⚠️ Prediction failed: {e}")