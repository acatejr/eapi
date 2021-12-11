import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """Thje api must have a healthcheck route.
    """
    resp = client.get("/healthcheck")
    assert resp.status_code == 200
    assert resp.json() == {"msg": "ok"}

def test_api_v1_gages():
    """The api must allow for retrieval of 1 one or all raingages
    for a specified watershed.
    """
    resp = client.get("/api/v1/gages/")
    assert resp.status_code == 200

    resp = client.get("/api/v1/gages/1/1")
    assert resp.status_code == 200
