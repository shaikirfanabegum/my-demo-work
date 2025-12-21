from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_version():
    r = client.get("/version")
    assert r.status_code == 200
    body = r.json()
    assert "app_version" in body
    assert "git_sha" in body

def test_predict_smoker_higher_risk():
    non_smoker = {"age": 40, "bmi": 25.0, "smoker": False}
    smoker = {"age": 40, "bmi": 25.0, "smoker": True}

    r1 = client.post("/predict", json=non_smoker)
    r2 = client.post("/predict", json=smoker)

    assert r1.status_code == 200
    assert r2.status_code == 200
    assert r2.json()["risk_score"] > r1.json()["risk_score"]
