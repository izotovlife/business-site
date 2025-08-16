# backend/middleware.py
from django.conf import settings
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class AdminTicketMiddleware(MiddlewareMixin):
    """
    Блокирует доступ к реальному ADMIN_URL, если нет флага в сессии,
    который проставляется через одноразовую ссылку.
    В остальных случаях возвращаем 404, чтобы скрыть факт наличия админки.
    """

    def process_request(self, request):
        admin_url = "/" + getattr(settings, "ADMIN_URL", "admin/").lstrip("/")
        # только точный префикс админки
        if request.path.startswith(admin_url):
            # если флаг установлен в сессии — пускаем
            if request.session.get("admin_ticket_ok") is True:
                return None
            # иначе маскируем под 404
            return JsonResponse({"detail": "Not found"}, status=404)
        return None
