#C:\Users\ASUS Vivobook\PycharmProjects\izotoff.ru\business_site\backend\core\serializers.py

from rest_framework import serializers
from .models import ServiceSection, PortfolioItem, Testimonial, Lead


class ServiceSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSection
        fields = "__all__"


class PortfolioItemSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PortfolioItem
        fields = ["id", "title", "description", "image", "image_url", "link"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class TestimonialSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Testimonial
        fields = ["id", "author", "role", "text", "avatar", "avatar_url"]

    def get_avatar_url(self, obj):
        request = self.context.get("request")
        if obj.avatar and request:
            return request.build_absolute_uri(obj.avatar.url)
        return None

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ["id", "name", "contact", "message", "source", "created_at"]
        read_only_fields = ["id", "created_at"]