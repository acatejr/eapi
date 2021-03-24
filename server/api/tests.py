from django.test import TestCase
from django.urls import reverse, resolve
import pytest


@pytest.mark.django_db
def test_api_index(client):
    """Test the index or root index of the api"""
    url = reverse("graphql")
    response = client.get(url)
    assert response.status_code == 200
