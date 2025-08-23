# Назначение: модель для хранения текущего slug админки; path: backend/security/models.py; реализует AdminGate singleton.
from django.db import models
from django.utils import timezone


class AdminGate(models.Model):
    singleton_id = models.PositiveSmallIntegerField(primary_key=True, default=1)
    current_slug = models.CharField(max_length=64, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_or_create_singleton(cls) -> "AdminGate":
        obj, _ = cls.objects.get_or_create(pk=1, defaults={"current_slug": ""})
        return obj

    def __str__(self) -> str:  # pragma: no cover
        return self.current_slug


class AdminLink(models.Model):
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField()
    issued_to_ip = models.GenericIPAddressField()
    used_at = models.DateTimeField(null=True, blank=True)

    def is_valid(self, ip: str) -> bool:
        return (
            self.is_active
            and self.issued_to_ip == ip
            and self.expires_at >= timezone.now()
        )

    def __str__(self):  # pragma: no cover
        return self.slug
