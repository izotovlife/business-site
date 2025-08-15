from rest_framework import viewsets
from .models import ServiceSection
from .serializers import ServiceSectionSerializer

class ServiceSectionViewSet(viewsets.ModelViewSet):
    queryset = ServiceSection.objects.all()
    serializer_class = ServiceSectionSerializer

