from .models import GPSRegis
from rest_framework import serializers

class GPSRegisSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSRegis
        fields = ('lat', 'lon', 'cel', 'usuario', 'fecha')