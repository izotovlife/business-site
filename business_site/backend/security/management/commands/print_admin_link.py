# Назначение: команда печати текущего URL админки; path: backend/security/management/commands/print_admin_link.py; использует utils.get_current_slug.
from django.core.management.base import BaseCommand

from ...utils import get_current_slug


class Command(BaseCommand):
    help = "Print current admin external URL"

    def handle(self, *args, **options):
        slug = get_current_slug()
        self.stdout.write(f"/{slug}/")
