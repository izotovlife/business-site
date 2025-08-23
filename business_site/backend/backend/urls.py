# Назначение: маршрутизация проекта; path: backend/backend/urls.py; оставлен внутренний путь админки и подключён API security.
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
)
from django.http import JsonResponse, HttpRequest


def index(_request: HttpRequest) -> JsonResponse:
    return JsonResponse({
        "name": "Izotov Business Site API",
        "version": "1.0.0",
        "docs": {"schema": "/api/schema/", "swagger": "/api/docs/", "redoc": "/api/redoc/"},
        "api": {"v1": "/api/v1/"},
        "status": "ok",
    })


def health(_request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "ok"})


urlpatterns = [
    # Служебные
    path("", index, name="index"),
    path("health/", health, name="health"),

    # API
    path("api/v1/", include("core.urls")),
    path("", include("security.urls")),

    # OpenAPI
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    # Реальный скрытый путь админки
    path(settings.ADMIN_INTERNAL_PATH.lstrip("/"), admin.site.urls),
]

# Media в DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
