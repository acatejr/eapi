import pytest

def test_index(client):
    """Test the web side index endpoint"""
    resp = client.get('/')
    assert resp.status == '200 OK'

def test_status(client):
    """Test the status endpoint"""
    assert client is not None
    resp = client.get('/status')
    assert resp.status == '200 OK'

def test_api_status(client):
    assert client is not None
    resp = client.get('/api/status', query='{status}')
    assert resp.status == '200 OK'
