from django.test import TestCase
from django.urls import reverse, resolve
from graphene.test import Client
from api.schema import schema
import pytest

def test_api_index():
    client = Client(schema)
    query = '''{status}'''
    response = client.execute(query)

    assert response == {'data': {'status': 'status'}}

# @pytest.mark.django_db
# def test_api_index(client):
#     """Test the index or root index of the api"""
#     url = reverse("graphql")
#     response = client.get(url)
#     assert response.status_code == 200
