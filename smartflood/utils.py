import json
from datetime import datetime

def calculate_risk(precip_values):
    avg = sum(precip_values) / len(precip_values)

    if avg > 20:
        return ("High", avg)
    elif avg > 5:
        return ("Medium", avg)
    return ("Low", avg)


def log_actions(action: str):
    with open("logs.txt", "a") as file:
        file.write(f"{datetime.now()} --> {action}\n")
