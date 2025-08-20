# backend/security/middleware.py
# Назначение: middleware для динамического внешнего адреса админки. Путь: backend/security/middleware.py.
# Изменения: переписывает запросы по slug на внутренний путь и запрещает прямой доступ.
from django.conf import settings
from django.http import HttpResponseNotFound
from typing import Callable

from .utils import get_current_slug


class DynamicAdminSlugMiddleware:
    """Маппит внешний slug на физический путь админки."""

    def __init__(self, get_response: Callable):
        self.get_response = get_response

    def __call__(self, request):
        admin_internal = settings.ADMIN_INTERNAL_PATH.rstrip("/")
        path = request.path
        rewritten = False
        external = None

        # Блокировка прямого доступа к внутреннему пути
        if path == admin_internal or path.startswith(admin_internal + "/"):
            if not getattr(request, "_via_dynamic_admin", False):
                return HttpResponseNotFound()
        else:
            slug = get_current_slug()
            candidate = f"/{slug}"
            if path == candidate or path.startswith(candidate + "/"):
                external = candidate
                # Переписываем путь на внутренний
                suffix = path[len(candidate):] or "/"
                new_path = admin_internal + suffix
                request.path_info = new_path
                request.path = new_path
                request.META["PATH_INFO"] = new_path
                setattr(request, "_via_dynamic_admin", True)
                rewritten = True

        response = self.get_response(request)

        # Если был редирект, перепишем Location обратно на slug
        if rewritten and external and response.has_header("Location"):
            location = response["Location"]
            response["Location"] = location.replace(admin_internal, external)
        return response
