import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

@pytest.mark.skip("Skipping api endpoint tests.")
def test_api_root():
    response = client.get("/")
    assert response.status_code == 200
