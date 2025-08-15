from rest_framework import serializers
from .models import ServiceSection

class ServiceSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSection
        fields = '__all__'
