from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="SmartTest-AI")

class Measurement(BaseModel):
    voltage: float
    current: float

@app.get("/")
def home():
    return {
        "project": "SmartTest-AI",
        "status": "running"
    }

@app.post("/measurements")
def receive_measurements(data: Measurement):
    print("New measurement received")
    print(f"Voltage: {data.voltage} V")
    print(f"Current: {data.current} A")

    return {
        "status": "success",
        "voltage": data.voltage,
        "current": data.current
    }