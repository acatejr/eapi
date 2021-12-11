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

def test_api_v1_wgew_gages():
    """The api must allow for retrieval of 1 one or all raingages
    for a specified watershed.
    """
    resp = client.get("/api/v1/wgewgages/")
    assert resp.status_code == 200

    resp = client.get("/api/v1/wgewgages/1/1")
    assert resp.status_code == 200

def test_api_v1_wgew_precip():
    """The api must allow for retrieval of precip events for a
    specified watershed id and raingage id"""

    resp = client.get("/api/v1/wgewprecip/1/1")
    assert resp.status_code == 200
