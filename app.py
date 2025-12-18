import streamlit as st
import matplotlib.pyplot as plt
from model import calculate_capacity, predict_sla_risk, forecast_backlog

st.title("SLA Risk Predictor & What-If Simulator")

st.write("Predict SLA risk and backlog trends using current workload data.")

# Inputs
wip = st.number_input("Current Work In Progress (cases)", min_value=0, value=120)
incoming_rate = st.number_input("Incoming cases per hour", min_value=0.0, value=20.0)
avg_time = st.number_input("Average processing time per case (minutes)", min_value=1.0, value=30.0)
agents = st.slider("Number of available agents", min_value=1, max_value=20, value=6)

# Processing
capacity = calculate_capacity(agents, avg_time)
risk = predict_sla_risk(wip, incoming_rate, capacity)
forecast = forecast_backlog(wip, incoming_rate, capacity)

# Output
st.subheader("Prediction Results")
st.write(f"**Estimated Processing Capacity:** {capacity:.2f} cases/hour")
st.write(f"**Predicted SLA Risk:** {risk}")

# Plot
st.subheader("Backlog Forecast (Next 6 Hours)")
fig, ax = plt.subplots()
ax.plot(range(1, 7), forecast)
ax.set_xlabel("Hours Ahead")
ax.set_ylabel("Expected Backlog")
st.pyplot(fig)
