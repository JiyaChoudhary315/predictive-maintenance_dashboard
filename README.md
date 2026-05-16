# EV Motor Predictive Maintenance Dashboard

A machine learning based predictive maintenance system for EV/Industrial motors using FastAPI, Streamlit, and Random Forest Classification.

## Features

- Real-time motor health prediction
- Fault detection system
- Interactive Streamlit dashboard
- Sensor telemetry visualization
- Machine learning based classification
- REST API using FastAPI

---

## Tech Stack

- Python
- FastAPI
- Streamlit
- Scikit-learn
- Pandas
- Plotly
- Joblib

---

## Parameters Used

- Temperature
- Vibration
- RPM
- Current

---

## Machine Learning Model

Random Forest Classifier trained on simulated motor telemetry data.

---

## Dashboard Preview

### Healthy Motor

![Healthy](screenshots/healthy.png)

---

### Fault Detection

![Fault](screenshots/fault.png)

---

### Telemetry Visualization

![Graphs](screenshots/graphs.png)

---

## How to Run

### Backend

```bash
cd backend
uvicorn app:app --reload