# backend/security/views.py
# Назначение: API для получения текущей ссылки админки. Путь: backend/security/views.py.
# Изменения: добавлен AdminLinkView на DRF.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .utils import get_current_slug


class AdminLinkView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.is_superuser:
            return Response(status=403)
        slug = get_current_slug()
        return Response({"admin_url": f"/{slug}/"})
