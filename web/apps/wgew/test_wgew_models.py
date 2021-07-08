import pytest
from apps.wgew.models import Raingage, PrecipEvent

@pytest.mark.django_db

class TestModels:

    def test_raingage_create(self):
        Raingage.objects.create(
            gage_id=1,
            watershed_id=1
        )

    def test_precipevent_create(self):
        """
        Raingage.objects.create(
            gage_id=1,
            watershed_id=1
        )
        """

        """
        rg = Raingage(gage_id=1, watershed_id=1)
        rg.save()
        """
        
        PrecipEvent.objects.create()
