# Назначение: корневой роутинг проекта (важна строка подключения админки)
# Путь: backend/backend/urls.py

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
    path("accounts/", include("django.contrib.auth.urls")),

    # API
    path("api/v1/", include("core.urls")),
    path("api/v1/", include("services.urls")),
    path("api/security/", include("security.urls")),

    # OpenAPI
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    # Реальный скрытый путь админки (ВАЖНО: слэш на конце)
    path(f"{settings.ADMIN_INTERNAL_PATH.strip('/')}/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
