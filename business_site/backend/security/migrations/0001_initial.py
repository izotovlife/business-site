# Назначение: начальная миграция для модели AdminGate; path: backend/security/migrations/0001_initial.py.
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdminGate",
            fields=[
                ("singleton_id", models.PositiveSmallIntegerField(primary_key=True, default=1, serialize=False)),
                ("current_slug", models.CharField(max_length=64, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
