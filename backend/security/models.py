# backend/security/models.py
# Назначение: модель для хранения текущего slug админки. Путь: backend/security/models.py.
# Изменения: добавлена модель AdminGate с singleton и временем обновления.
from django.db import models


class AdminGate(models.Model):
    singleton_id = models.PositiveSmallIntegerField(
        primary_key=True, default=1, editable=False
    )
    current_slug = models.CharField(max_length=64, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_or_create_singleton(cls) -> "AdminGate":
        obj, _created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self) -> str:  # pragma: no cover - для удобства
        return self.current_slug
