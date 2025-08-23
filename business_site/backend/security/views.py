# Назначение: API для выдачи текущего slug админки; path: backend/security/views.py.
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import get_current_slug


class AdminLinkView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        slug = get_current_slug()
        return Response({"admin_url": f"/{slug}/"})
