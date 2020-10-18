from rest_framework import serializers
from datacollection.models import Datacollection
class GetSerializer(serializers.Serializer):
    class Meta:
        model = Datacollection
        fields = '__all__'