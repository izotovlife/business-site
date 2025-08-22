# Назначение: middleware, пропускающее в админку только после одноразовой ссылки
# Путь: backend/security/middleware.py

from django.conf import settings
from django.http import Http404

class DynamicAdminSlugMiddleware:
    """
    Блокирует прямой доступ к реальной админке (/_admin/...)
    пока не будет открыт «гейт» через одноразовую ссылку /admin/open/<token>/.
    После успешного открытия во view ставится флаг в сессии.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # нормализуем префикс админки со слэшем в начале и конце
        admin_path = settings.ADMIN_INTERNAL_PATH.strip("/")
        self.admin_prefix = f"/{admin_path}/" if admin_path else "/_admin/"

    def __call__(self, request):
        path = request.path

        # Разрешаем сам «гейт» и выдачу ссылки
        if path.startswith("/admin/open/") or path.startswith("/api/admin-link"):
            return self.get_response(request)

        # Если это обращение к реальной админке — требуем флаг в сессии
        if path.startswith(self.admin_prefix):
            if request.session.get("admin_gate_ok"):
                return self.get_response(request)
            # Нет флага — прячем админку
            raise Http404()

        return self.get_response(request)
