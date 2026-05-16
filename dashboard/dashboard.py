import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Page config
st.set_page_config(
    page_title="EV Predictive Maintenance",
    layout="wide"
)

# Load dataset
df = pd.read_csv("data/sensor_data.csv")

# Load model
model = joblib.load("../models/motor_health_model.pkl")

# Title
st.title("EV Motor Predictive Maintenance Dashboard")

st.markdown("### Real-Time Industrial Motor Health Monitoring System")

# Sidebar
st.sidebar.header("Input Motor Parameters")

temperature = st.sidebar.slider("Temperature (°C)", 0, 150, 70)

vibration = st.sidebar.slider("Vibration", 0, 10, 4)

rpm = st.sidebar.slider("RPM", 0, 6000, 3000)

current = st.sidebar.slider("Current (A)", 0, 50, 20)

# Prediction
data = np.array([[temperature, vibration, rpm, current]])

prediction = model.predict(data)

# Status section
st.subheader("Motor Health Status")

if prediction[0] == 1:

    st.success("Motor Status: HEALTHY")

else:

    st.error("Motor Status: FAULT DETECTED")

# Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Temperature", f"{temperature} °C")

col2.metric("Vibration", vibration)

col3.metric("RPM", rpm)

col4.metric("Current", f"{current} A")

# Dataset preview
st.subheader("Sensor Dataset Preview")

st.dataframe(df.head())

# Graphs
st.subheader("Telemetry Visualization")

st.line_chart(df["temperature"])

st.line_chart(df["vibration"])

st.line_chart(df["rpm"])

st.line_chart(df["current"])