# backend/core/views.py
from django.conf import settings
from django.core.mail import EmailMessage
import logging
from threading import Thread

from rest_framework import viewsets, mixins, filters

from .models import ServiceSection, PortfolioItem, Testimonial, Lead
from .serializers import (
    ServiceSectionSerializer,
    PortfolioItemSerializer,
    TestimonialSerializer,
    LeadSerializer,
)

log = logging.getLogger(__name__)


def _send_mail_async(subject: str, body: str, to_email: str) -> None:
    """
    Неблокирующая отправка письма в отдельном потоке.
    HTTP-ответ клиенту не ждёт SMTP.
    """
    def worker():
        try:
            msg = EmailMessage(subject=subject, body=body, to=[to_email])
            # если в settings задан EMAIL_TIMEOUT — Django его применит
            msg.send(fail_silently=True)
        except Exception as e:
            log.warning("Email sending failed: %s", e, exc_info=True)

    Thread(target=worker, daemon=True).start()


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

        # Формируем письмо
        subject = "Новая заявка с сайта"
        body = (
            f"Имя: {lead.name}\n"
            f"Контакт: {lead.contact}\n"
            f"Сообщение: {lead.message}"
        )
        from_email = getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@example.com")
        to_email = getattr(settings, "NOTIFY_TO", "izotovlife@yandex.ru")

        # Стартуем отправку в фоне (не блокируя HTTP-ответ)
        _send_mail_async(subject, body, to_email)
