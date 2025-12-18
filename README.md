# SLA Risk Predictor & What-If Simulator

This project implements a simple predictive system to estimate SLA breach risk
in high-volume operational workflows.

The application uses current workload data and resource availability to:
- Forecast backlog trends
- Classify SLA risk levels (Low / Medium / High)
- Simulate “what-if” scenarios by adjusting available resources

The goal is to provide early warning signals that help operations teams
take proactive decisions instead of reacting after SLA violations occur.

## How it Works
Input data such as work-in-progress, incoming case rate, average processing
time, and number of agents are processed using lightweight predictive logic.
The results are visualized through an interactive Streamlit dashboard.

## Tech Stack
- Python
- Streamlit
- Matplotlib

## Running the Application
```bash
pip install -r requirements.txt
streamlit run app.py

##Use case:

Operations teams managing high-volume workflows often struggle to anticipate
SLA breaches due to fluctuating case arrivals and limited resource visibility.
This system helps operations managers proactively monitor workload pressure
and identify potential SLA risks before violations occur.

By analyzing current work-in-progress, incoming case rates, and available
agent capacity, the application forecasts backlog trends and classifies SLA
risk levels. Managers can use the built-in “what-if” simulation to evaluate
the impact of adding or reallocating agents in real time.

This enables faster, data-driven decisions that reduce backlog growth,
improve SLA compliance, and minimize reactive firefighting in daily operations.
