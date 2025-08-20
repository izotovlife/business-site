# Назначение: утилиты для генерации и хранения slug админки; path: backend/security/utils.py; реализует кэширование и ротацию.
import secrets
from typing import Optional
from django.core.cache import cache

from .models import AdminGate

CACHE_KEY = "dynamic_admin_slug"
CACHE_TTL = 60 * 60  # 1 час


def generate_slug(length: int = 16) -> str:
    return secrets.token_urlsafe(length)[:length]


def get_current_slug() -> str:
    slug: Optional[str] = cache.get(CACHE_KEY)
    if slug:
        return slug
    gate = AdminGate.get_or_create_singleton()
    if not gate.current_slug:
        gate.current_slug = generate_slug()
        gate.save(update_fields=["current_slug"])
    slug = gate.current_slug
    cache.set(CACHE_KEY, slug, CACHE_TTL)
    return slug


def rotate_slug() -> str:
    slug = generate_slug()
    gate = AdminGate.get_or_create_singleton()
    gate.current_slug = slug
    gate.save(update_fields=["current_slug", "updated_at"])
    cache.set(CACHE_KEY, slug, CACHE_TTL)
    return slug
