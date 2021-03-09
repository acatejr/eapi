import pytest

def test_init_app(client):
    """Simple test just to make sure that a test client
    can be instantiated.
    """
    assert client is not None
