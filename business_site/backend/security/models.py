# Назначение: модель для хранения текущего slug админки; path: backend/security/models.py; реализует AdminGate singleton.
from django.db import models


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
