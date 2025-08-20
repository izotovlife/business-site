# backend/security/tests/test_middleware_rewrite.py
# Назначение: проверка работы middleware динамического slug. Путь: backend/security/tests/test_middleware_rewrite.py.
# Изменения: новый тест на переписывание пути и блокировку прямого доступа.
from django.conf import settings
from django.test import TestCase

from security.utils import rotate_slug


class MiddlewareRewriteTests(TestCase):
    def test_middleware_rewrite(self):
        slug = rotate_slug()

        resp = self.client.get(f"/{slug}/", follow=True)
        self.assertContains(resp, "name=\"username\"", status_code=200)

        resp2 = self.client.get(settings.ADMIN_INTERNAL_PATH, follow=True)
        self.assertEqual(resp2.status_code, 404)
