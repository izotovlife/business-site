# Назначение: middleware для динамического slug админки; path: backend/security/middleware.py; переписывает внешний путь на внутренний.
from django.http import Http404
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

from .utils import get_current_slug


class DynamicAdminSlugMiddleware(MiddlewareMixin):
    def process_request(self, request):
        internal = settings.ADMIN_INTERNAL_PATH
        if request.path.startswith(internal):
            if not getattr(request, "_via_dynamic_admin", False):
                raise Http404()
            return

        slug = get_current_slug()
        slug_prefix = f"/{slug}"
        if request.path == slug_prefix or request.path.startswith(slug_prefix + "/"):
            tail = request.path[len(slug_prefix):] or "/"
            new_path = internal.rstrip("/") + tail
            request.path = new_path
            request.path_info = new_path
            request._via_dynamic_admin = True
