from rest_framework import serializers
from .models import Service, Lead


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "slug", "title", "short", "description", "price_from"]


class LeadCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ["name", "email", "phone", "service", "message", "consent"]

    def validate(self, attrs):
        if not attrs.get("name") and not (attrs.get("phone") or attrs.get("email")):
            raise serializers.ValidationError(
                "Нужно указать хотя бы имя и телефон или email."
            )
        if not attrs.get("consent"):
            raise serializers.ValidationError(
                "Нужно согласиться с правилами обработки данных."
            )
        return attrs
