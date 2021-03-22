import pytest

from django.urls import reverse, resolve


@pytest.mark.django_db
def test_api_index(client):
    """Test the index or root index of the api"""
    found = resolve("/")
    print(dir(found))
    assert found.func, api_index
    pytest.fail("Finish me!")

# @pytest.mark.django_db
# def test_api_status(client):
#     """Test the index or root index of the api"""
#     pytest.fail("Implement me!")
