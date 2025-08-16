# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
)
from django.http import JsonResponse, HttpRequest
import logging

from .views_security import create_admin_link, use_admin_link, api_login, api_logout

log = logging.getLogger(__name__)

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

def fake_admin(request: HttpRequest) -> JsonResponse:
    ip = request.META.get("REMOTE_ADDR") or request.META.get("HTTP_X_FORWARDED_FOR")
    ua = request.META.get("HTTP_USER_AGENT", "-")
    log.warning("Fake admin hit: ip=%s ua=%s path=%s", ip, ua, request.path)
    return JsonResponse({"detail": "Not found"}, status=404)

urlpatterns = [
    # Служебные
    path("", index, name="index"),
    path("health/", health, name="health"),

    # API
    path("api/v1/", include("core.urls")),

    # OpenAPI
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    # Аутентификация (login/logout)
    path("accounts/login/", api_login, name="login"),
    path("accounts/logout/", api_logout, name="logout"),

    # Одноразовые ссылки на админку
    path("admin-link/", create_admin_link, name="create-admin-link"),        # отдать одноразовый URL (только staff)
    path("admin-ticket/<str:token>/", use_admin_link, name="use-admin-link"),# перейти по одноразовому URL

    # Ловушка на /admin/
    path("admin/", fake_admin, name="fake-admin"),
]

# Реальный скрытый путь админки (фиксированный, но никому не выдаём напрямую)
admin_url = getattr(settings, "ADMIN_URL", "admin/")
urlpatterns += [path(admin_url, admin.site.urls)]

# Media в DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
