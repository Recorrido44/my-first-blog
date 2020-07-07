from .serializers import GPSRegisSerializer
from .models import GPSRegis
from rest_framework import generics


class GPSRegisList(generics.ListCreateAPIView):
    queryset = GPSRegis.objects.all()
    serializer_class = GPSRegisSerializer


class GPSRegisDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GPSRegis.objects.all()
    serializer_class = GPSRegisSerializer