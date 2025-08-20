# Назначение: конфигурация приложения security; path: backend/security/apps.py; в ready подключаются сигналы.
from django.apps import AppConfig


class SecurityConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "security"

    def ready(self) -> None:  # pragma: no cover
        from . import signals  # noqa: F401
