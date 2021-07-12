import pytest
from apps.wgew.models import Raingage, PrecipEvent

@pytest.mark.django_db

class TestModels:

    def test_raingage_create(self):
        Raingage.objects.create(
            gage_id=1,
            watershed_id=1
        )
   
    def test_raingage_read(self):
        instance = Raingage.objects.create(
            gage_id=1,
            watershed_id=1
        )
        rg = Raingage.objects.get(id=instance.id)
        assert rg is not None

    def test_raingage_update(self):
        instance = Raingage.objects.create(
            gage_id=1,
            watershed_id=1
        )

        rg = Raingage.objects.get(id=instance.id)
        rg.watershed_id = 2
        rg.save()

        assert rg.watershed_id == 2
 
    def test_raingage_delete(self):
        rg = Raingage.objects.create(
            gage_id=1,
            watershed_id=1
        )

        assert rg is not None
        rg.delete()

        with pytest.raises(Raingage.DoesNotExist):
            Raingage.objects.get(id=1)
  
    def test_precipevent_create(self):
        PrecipEvent.objects.create(duration=2.3)

    def test_precipevent_read(self):
        instance = PrecipEvent.objects.create(duration=1)
        pe = PrecipEvent.objects.get(id=instance.id)
        assert pe is not None

    def test_precipevent_update(self):
        instance = PrecipEvent.objects.create(duration=1)
        instance.duration = 2
        instance.save()

        pe = PrecipEvent.objects.get(id=instance.id)
        assert pe.duration == instance.duration

    def test_precipevent_delete(self):
        pe = PrecipEvent.objects.create(id=1)
        pe.delete()
        with pytest.raises(PrecipEvent.DoesNotExist):
            PrecipEvent.objects.get(id=1)

