from django.test import TestCase
from django.urls import reverse, resolve
from graphene.test import Client
from apps.api.schema import schema
import pytest

def test_api_index():
    """Test that the graphql api status query is working."""
    client = Client(schema)
    query = '''{status}'''
    response = client.execute(query)
    print(dir(response))
    assert response == {'data': {'status': 'status'}}
    assert False

def test_wgew_all_raingages():
    """Test query for all WGEW raingages"""
    pytest.fail("Implement me!")

# @pytest.mark.django_db
# def test_api_index(client):
#     """Test the index or root index of the api"""
#     url = reverse("graphql")
#     response = client.get(url)
#     assert response.status_code == 200
