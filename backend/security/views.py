# Назначение: API и обработчик «гейта» для защищённого входа в админку
# Путь: backend/security/views.py

from django.conf import settings
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.shortcuts import redirect
from django.utils.crypto import get_random_string
from django.views import View

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


def _admin_base_path() -> str:
    # '/_admin/'
    return f"/{settings.ADMIN_INTERNAL_PATH.strip('/')}/"


class AdminLinkView(APIView):
    """
    Выдаёт одноразовую ссылку для входа в админку.
    DEV (DEBUG=True): доступен всем.
    PROD (DEBUG=False): только staff.
    """
    def get_permissions(self):
        if settings.DEBUG:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def get(self, request):
        signer = TimestampSigner()
        # случайная строка + подпись с меткой времени
        token = signer.sign(get_random_string(32))
        # Переход по этой ссылке откроет «гейт» и редиректит в реальную админку
        return Response({"admin_url": f"/admin/open/{token}/"})


class OpenAdminView(View):
    """
    Использование одноразовой ссылки: проверяет подпись и срок годности,
    ставит флаг в сессии и перенаправляет на реальную админку.
    """
    MAX_AGE_SECONDS = 5 * 60  # 5 минут

    def get(self, request, token: str):
        signer = TimestampSigner()
        try:
            signer.unsign(token, max_age=self.MAX_AGE_SECONDS)
        except (BadSignature, SignatureExpired):
            # Либо токен подделан, либо протух — не пускаем
            return redirect("/")  # можно вернуть 404, если хочешь полностью скрыть поведение

        # Открываем «ворота» на текущую сессию
        request.session["admin_gate_ok"] = True
        request.session.modified = True

        # В реальную админку (/_admin/) — там уже форма логина Django
        return redirect(_admin_base_path())
