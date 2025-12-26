from rest_framework import viewsets
from .models import Governorate, City
from .serializers import GovernorateSerializer, CitySerializer

class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    """Public API to get all Yemen Governorates and Cities"""
    queryset = Governorate.objects.prefetch_related('cities').all()
    serializer_class = GovernorateSerializer
    pagination_class = None # Return all at once