# Назначение: сигналы безопасности; path: backend/security/signals.py; при логине суперпользователя вращает slug.
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

from .utils import rotate_slug


@receiver(user_logged_in)
def rotate_on_admin_login(sender, request, user, **kwargs):
    if request is None:
        return
    if request.path.startswith(settings.ADMIN_INTERNAL_PATH) and getattr(user, "is_superuser", False):
        rotate_slug()
