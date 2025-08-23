from django.conf import settings
from django.core.mail import send_mail

from rest_framework import viewsets, mixins, filters

from .models import ServiceSection, PortfolioItem, Testimonial, Lead
from .serializers import (
    ServiceSectionSerializer,
    PortfolioItemSerializer,
    TestimonialSerializer,
    LeadSerializer,
)


class ServiceSectionViewSet(viewsets.ModelViewSet):
    queryset = ServiceSection.objects.all().order_by("id")
    serializer_class = ServiceSectionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "content"]
    ordering_fields = ["id", "title"]


class PortfolioItemViewSet(viewsets.ModelViewSet):
    queryset = PortfolioItem.objects.all().order_by("id")
    serializer_class = PortfolioItemSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["id", "title"]


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all().order_by("id")
    serializer_class = TestimonialSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["author", "role", "text"]
    ordering_fields = ["id", "author"]


class LeadViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Создание лида: POST /api/v1/leads/
    """
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    http_method_names = ["post"]

    def perform_create(self, serializer):
        lead = serializer.save()
        # отправка уведомления на email
        send_mail(
            subject="Новая заявка с сайта",
            message=(
                f"Имя: {lead.name}\n"
                f"Контакт: {lead.contact}\n"
                f"Сообщение: {lead.message}"
            ),
            from_email=getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@example.com"),
            recipient_list=[getattr(settings, "NOTIFY_TO", "izotovlife@yandex.ru")],
            fail_silently=False,
        )
