from fastapi import FastAPI
import joblib
import numpy as np

# Create FastAPI app
app = FastAPI()

# Load trained model
model = joblib.load("../models/motor_health_model.pkl")

@app.get("/")
def home():

    return {
        "message": "EV Motor Predictive Maintenance API"
    }

@app.post("/predict")
def predict(
    temperature: float,
    vibration: float,
    rpm: float,
    current: float
):

    # Prepare data
    data = np.array([[temperature, vibration, rpm, current]])

    # Predict
    prediction = model.predict(data)

    # Output result
    if prediction[0] == 1:
        status = "Healthy"

    else:
        status = "Fault Detected"

    return {
        "motor_status": status
    }