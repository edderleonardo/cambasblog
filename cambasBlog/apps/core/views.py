from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import CountrySerializer
from .models import Country


class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [AllowAny]
