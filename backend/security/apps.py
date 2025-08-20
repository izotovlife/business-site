# backend/security/apps.py
# Назначение: конфигурация приложения security. Путь: backend/security/apps.py.
# Изменения: создан AppConfig с подключением signals в ready().
from django.apps import AppConfig


class SecurityConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "security"

    def ready(self) -> None:  # pragma: no cover - импорт побочных эффектов
        from . import signals  # noqa: F401
