from rest_framework.serializers import Serializer
from rest_framework.serializers import IntegerField, CharField, DecimalField


class RaingageSerializer(Serializer):

    id = IntegerField(read_only=True)

    name = CharField()

    code = CharField()

    latitude = DecimalField(max_digits=25, decimal_places=5)

    longitude = DecimalField(max_digits=25, decimal_places=5)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class PrecipEventSerializer(Serializer):

    id = IntegerField(read_only=True)

    year = IntegerField()

    month = IntegerField()

    precip = DecimalField(max_digits=50, decimal_places=10)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
