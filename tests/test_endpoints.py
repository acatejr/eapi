import pytest
from fastapi.testclient import TestClient
from starlette.testclient import TestClient as GraphQlTestClient

from app.main import app

client = TestClient(app)

def test_site_root():
    response = client.get("/")
    assert response.status_code == 200

def test_api_root():
    client = GraphQlTestClient(app)    
    response = client.get("/?query={}")
    assert response.status_code == 200

def test_api_status():
    client = GraphQlTestClient(app)    
    response = client.get("/?query={status}")
    assert response.status_code == 200

def test_get_raingage():
    client = GraphQlTestClient(app)    
    response = client.get("/?query={wgew_raingage_id=1}")
    assert response.status_code == 200
