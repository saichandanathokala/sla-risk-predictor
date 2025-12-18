import numpy as np
def calculate_capacity(num_agents, avg_time_minutes):
    # cases processed per hour
    return (60 / avg_time_minutes) * num_agents


def predict_sla_risk(wip, incoming_rate, capacity):
    backlog_change = incoming_rate - capacity

    if backlog_change <= 0:
        return "Low"
    elif backlog_change <= capacity * 0.3:
        return "Medium"
    else:
        return "High"


def forecast_backlog(wip, incoming_rate, capacity, hours=6):
    backlog = []
    current = wip

    for _ in range(hours):
        current = current + incoming_rate - capacity
        current = max(current, 0)
        backlog.append(current)

    return backlog
