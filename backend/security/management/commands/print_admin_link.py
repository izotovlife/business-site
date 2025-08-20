# backend/security/management/commands/print_admin_link.py
# Назначение: команда вывода текущего внешнего URL админки. Путь: backend/security/management/commands/print_admin_link.py.
# Изменения: новая management-команда.
from django.core.management.base import BaseCommand

from security.utils import get_current_slug


class Command(BaseCommand):
    help = "Print current external admin URL"

    def handle(self, *args, **options):  # pragma: no cover - вывод в консоль
        slug = get_current_slug()
        self.stdout.write(f"/{slug}/")
