from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI(
    title="Autonomous Portfolio Rebalancing Agent",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home():
    return {
        "message": "Autonomous Portfolio Rebalancing Agent is Running"
    }


@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }
