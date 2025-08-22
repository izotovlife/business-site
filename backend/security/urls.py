# Назначение: URL-ы security (выдача ссылки и «гейт»)
# Путь: backend/security/urls.py

from django.urls import path
from .views import AdminLinkView, OpenAdminView

app_name = "security"

urlpatterns = [
    # JSON-эндпоинт → {"admin_url": "/admin/open/<token>/"}
    path("api/admin-link", AdminLinkView.as_view(), name="admin_link"),

    # Одноразовая ссылка, открывающая доступ к реальной админке
    path("admin/open/<path:token>/", OpenAdminView.as_view(), name="open_admin"),
]
