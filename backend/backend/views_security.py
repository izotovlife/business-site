# backend/views_security.py
import secrets
from django.conf import settings
from django.core.cache import cache
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, HttpRequest
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

# Настройки одноразовых ссылок (можно вынести в settings)
ADMIN_TICKET_TTL_SECONDS = getattr(settings, "ADMIN_TICKET_TTL_SECONDS", 300)  # 5 минут
ADMIN_TICKET_PREFIX = getattr(settings, "ADMIN_TICKET_PREFIX", "adm-")

def staff_check(u):  # кто имеет право генерировать ссылку
    return u.is_active and u.is_staff

@login_required
@user_passes_test(staff_check)
def create_admin_link(request: HttpRequest) -> JsonResponse:
    """
    Создаёт одноразовый токен и отдаёт URL вида /admin-ticket/<token>/
    Этот endpoint должен быть доступен только staff-пользователям.
    """
    token = ADMIN_TICKET_PREFIX + secrets.token_urlsafe(24)
    cache.set(f"admin_ticket:{token}", True, timeout=ADMIN_TICKET_TTL_SECONDS)
    one_time_url = reverse("use-admin-link", args=[token])
    expires_at = (timezone.now() + timedelta(seconds=ADMIN_TICKET_TTL_SECONDS)).isoformat()
    # Если браузер ожидает HTML (например, редирект после логина), сразу ведём в админку
    accept = request.headers.get("Accept", "")
    if "application/json" not in accept:
        return redirect(one_time_url)
    return JsonResponse({"url": one_time_url, "expires_at": expires_at})

def use_admin_link(request: HttpRequest, token: str):
    """
    Валидирует токен из cache, помечает сессию, удаляет токен и
    редиректит на реальную админку (без раскрытия пути).
    """
    key = f"admin_ticket:{token}"
    if cache.get(key):
        # активируем билет в сессии и сжигаем токен
        request.session["admin_ticket_ok"] = True
        cache.delete(key)
        return redirect(reverse("admin:index"))
    return JsonResponse({"detail": "Expired or invalid link"}, status=404)
