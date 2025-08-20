# backend/security/tests/test_admin_link_api.py
# Назначение: проверка API получения ссылки админки. Путь: backend/security/tests/test_admin_link_api.py.
# Изменения: новый тест для AdminLinkView.
from django.contrib.auth import get_user_model
from django.test import TestCase

from security.utils import rotate_slug


class AdminLinkAPITests(TestCase):
    def test_admin_link_api(self):
        rotate_slug()
        User = get_user_model()
        admin = User.objects.create_superuser("admin", "admin@example.com", "pass")
        user = User.objects.create_user("user", "user@example.com", "pass")

        self.client.force_login(admin)
        resp = self.client.get("/api/admin-link")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["admin_url"].startswith("/"))

        self.client.logout()
        self.client.force_login(user)
        resp2 = self.client.get("/api/admin-link")
        self.assertEqual(resp2.status_code, 403)
