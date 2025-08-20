# backend/security/urls.py
# Назначение: маршруты приложения security. Путь: backend/security/urls.py.
# Изменения: добавлен эндпоинт API для получения ссылки админки.
from django.urls import path

from .views import AdminLinkView

urlpatterns = [
    path("api/admin-link", AdminLinkView.as_view(), name="admin-link"),
]
