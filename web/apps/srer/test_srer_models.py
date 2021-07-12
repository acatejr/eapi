import pytest
from apps.srer.models import Raingage, PrecipEvent

@pytest.mark.django_db

class TestModels:

    def test_raingage_create(self):
        Raingage.objects.create()

    def test_raingage_read(self):
        instance = Raingage.objects.create()
        rg = Raingage.objects.get(id=instance.id)
        assert rg is not None
        assert rg.id == instance.id

    def test_raingage_update(self):
        instance = Raingage.objects.create(station_code='code')
        rg = Raingage.objects.get(id=instance.id)
        assert rg.station_code == 'code'

        rg.station_code = 'new_code'
        rg.save()

        assert rg.station_code == 'new_code'
        instance = Raingage.objects.get(id=instance.id)
        assert instance.station_code == 'new_code'

    def test_raingage_delete(self):
        instance = Raingage.objects.create(station_code='code')
        gage_id = instance.id
        assert instance is not None
        instance.delete()
        with pytest.raises(Raingage.DoesNotExist):
            Raingage.objects.get(id=gage_id)

    def test_precipevent_create(self):
        PrecipEvent.objects.create()

    def test_precipevent_read(self):
        instance = PrecipEvent.objects.create()
        pe = PrecipEvent.objects.get(id=instance.id)
        assert pe is not None
        assert pe.id == instance.id

    def test_precipevent_update(self):
         instance = PrecipEvent.objects.create(year=1980)
         pe = PrecipEvent.objects.get(id=instance.id)
         assert pe is not None
         pe.year = 1990
         pe.save()
         assert pe.year == 1990
         instance = PrecipEvent.objects.get(id=pe.id)
         assert instance.year == 1990

    def test_precipevent_delete(self):
        instance = PrecipEvent.objects.create(year=2000)
        pe_id = instance.id
        assert instance is not None
        instance.delete()
        with pytest.raises(PrecipEvent.DoesNotExist):
            PrecipEvent.objects.get(id=pe_id)
