import os
from fastapi import FastAPI, Response, Request
from pydantic import BaseModel, Field
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

APP_VERSION = os.getenv("APP_VERSION", "dev")
GIT_SHA = os.getenv("GIT_SHA", "unknown")

# ✅ SINGLE FastAPI app
app = FastAPI(title="AI/ML Inference API Demo", version=APP_VERSION)

# -------------------------
# Prometheus Metrics
# -------------------------
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"]
)

@app.middleware("http")
async def count_requests(request: Request, call_next):
    response = await call_next(request)
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path
    ).inc()
    return response

@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )

# -------------------------
# API Models
# -------------------------
class PredictRequest(BaseModel):
    age: int = Field(ge=0, le=120)
    bmi: float = Field(ge=10, le=80)
    smoker: bool

class PredictResponse(BaseModel):
    risk_score: float
    model_version: str

# -------------------------
# API Endpoints
# -------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"app_version": APP_VERSION, "git_sha": GIT_SHA}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    base = 0.15
    base += (req.age / 120.0) * 0.35
    base += ((req.bmi - 10.0) / (80.0 - 10.0)) * 0.35
    base += 0.15 if req.smoker else 0.0
    risk = max(0.0, min(1.0, base))
    return PredictResponse(
        risk_score=round(risk, 4),
        model_version="mock-v1"
    )

