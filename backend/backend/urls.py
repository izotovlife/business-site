# backend/backend/urls.py
# Назначение: корневые URL-паттерны проекта. Путь: backend/backend/urls.py.
# Изменения: админка доступна только по внутреннему пути "_admin/", удалены одноразовые ссылки,
# подключены health, core.urls и security.urls; внешние slug'и обрабатываются middleware.
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from django.http import JsonResponse, HttpRequest
import logging

log = logging.getLogger(__name__)


def index(_request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        {
            "name": "Izotov Business Site API",
            "version": "1.0.0",
            "docs": {
                "schema": "/api/schema/",
                "swagger": "/api/docs/",
                "redoc": "/api/redoc/",
            },
            "api": {"v1": "/api/v1/"},
            "status": "ok",
        }
    )


def health(_request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("", index, name="index"),
    path("health/", health, name="health"),
    path("api/v1/", include("core.urls")),
    # OpenAPI
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # API безопасности
    path("", include("security.urls")),
    # Физический путь админки
    path(settings.ADMIN_INTERNAL_PATH.lstrip("/"), admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
