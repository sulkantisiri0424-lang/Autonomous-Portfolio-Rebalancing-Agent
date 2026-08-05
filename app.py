from fastapi import FastAPI

app = FastAPI(
    title="Autonomous Portfolio Rebalancing Agent",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Autonomous Portfolio Rebalancing Agent",
        "status": "Running Successfully"
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }
