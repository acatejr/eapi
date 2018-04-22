from rest_framework.serializers import Serializer
from rest_framework.serializers import IntegerField, CharField, DecimalField
from rest_framework.serializers import DateField, TimeField

class RaingageSerializer(Serializer):

    id = IntegerField(read_only=True)

    watershed_id = CharField()

    gage_id = CharField()

    latitude = DecimalField(max_digits=25, decimal_places=5)

    longitude = DecimalField(max_digits=25, decimal_places=5)

    elevation = IntegerField()

    err = DecimalField(max_digits=5, decimal_places=1)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class PrecipEventSerializer(Serializer):

    id = IntegerField(read_only=True)

    event_date = DateField()

    event_time = TimeField()

    duration = DecimalField(max_digits=15, decimal_places=5)

    depth = DecimalField(max_digits=15, decimal_places=5)

    time_est = CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
