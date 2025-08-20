# Назначение: URLы приложения security; path: backend/security/urls.py.
from django.urls import path

from .views import AdminLinkView

urlpatterns = [
    path("api/admin-link", AdminLinkView.as_view()),
]
