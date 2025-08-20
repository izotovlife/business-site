# backend/security/utils.py
# Назначение: вспомогательные функции для управления slug админки. Путь: backend/security/utils.py.
# Изменения: генерация, получение из кэша и ротация slug.
import secrets
from django.core.cache import cache
from .models import AdminGate

CACHE_KEY = "security:admin_slug"
CACHE_TTL = 60 * 60  # 1 час


def generate_slug(length: int = 32) -> str:
    """Генерирует безопасный slug указанной длины."""
    return secrets.token_urlsafe(length)[:length]


def get_current_slug() -> str:
    """Возвращает текущий slug из кэша или базы."""
    slug = cache.get(CACHE_KEY)
    if slug:
        return slug
    gate = AdminGate.get_or_create_singleton()
    slug = gate.current_slug
    if not slug:
        slug = rotate_slug()
    else:
        cache.set(CACHE_KEY, slug, CACHE_TTL)
    return slug


def rotate_slug(length: int = 32) -> str:
    """Генерирует новый slug, сохраняет в БД и кэше."""
    slug = generate_slug(length)
    gate = AdminGate.get_or_create_singleton()
    gate.current_slug = slug
    gate.save(update_fields=["current_slug", "updated_at"])
    cache.set(CACHE_KEY, slug, CACHE_TTL)
    return slug
