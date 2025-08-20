# backend/security/signals.py
# Назначение: сигналы безопасности. Путь: backend/security/signals.py.
# Изменения: ротация slug при входе суперпользователя через админку.
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.conf import settings

from .utils import rotate_slug


@receiver(user_logged_in)
def rotate_slug_on_login(sender, request, user, **kwargs):
    if request and request.path.startswith(settings.ADMIN_INTERNAL_PATH) and user.is_superuser:
        rotate_slug()
