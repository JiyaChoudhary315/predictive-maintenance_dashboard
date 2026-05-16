import pandas as pd
import numpy as np

# Reproducible random values
np.random.seed(42)

# Number of rows
rows = 1000

# Simulated motor sensor values
temperature = np.random.normal(70, 10, rows)
vibration = np.random.normal(4, 1, rows)
rpm = np.random.normal(3000, 500, rows)
current = np.random.normal(20, 5, rows)

# Motor health condition
health = []

for t, v in zip(temperature, vibration):

    if t > 90 or v > 6:
        health.append(0)

    else:
        health.append(1)

# Create dataframe
df = pd.DataFrame({
    "temperature": temperature,
    "vibration": vibration,
    "rpm": rpm,
    "current": current,
    "health": health
})

# Save dataset
df.to_csv("motor_data.csv", index=False)

print(df.head())