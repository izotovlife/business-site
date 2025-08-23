from django.urls import path
from .views import create_admin_link, use_admin_link

app_name = "security"

urlpatterns = [
    path("admin-link/", create_admin_link, name="create_admin_link"),
    path("<slug:slug>/", use_admin_link, name="use_admin_link"),
]
