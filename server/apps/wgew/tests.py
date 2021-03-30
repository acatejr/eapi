from django.test import TestCase
import pytest
from apps.wgew.models import Raingage

@pytest.mark.django_db
def test_init_raingage_model():
    """Make sure a wgew raingage object can be instantiated"""
    rg = Raingage()
    assert rg is not None

@pytest.mark.django_db
def test_create_raingage():
    """Make sure we can create wgew raingages"""
    gage = Raingage(gage_id=1)
    gage.save()
    assert gage is not None
    found_gage = Raingage.objects.filter(gage_id=1)[0]
    assert found_gage.gage_id == 1
    gage.delete()
