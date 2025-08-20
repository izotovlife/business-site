# backend/security/tests/test_rotate_on_login.py
# Назначение: проверка ротации slug при входе суперпользователя. Путь: backend/security/tests/test_rotate_on_login.py.
# Изменения: новый тест на сигнал user_logged_in.
from django.contrib.auth import get_user_model
from django.test import TestCase

from security.utils import rotate_slug, get_current_slug


class RotateOnLoginTests(TestCase):
    def test_rotate_on_login(self):
        User = get_user_model()
        User.objects.create_superuser(
            username="admin", email="admin@example.com", password="pass1234"
        )

        slug_before = rotate_slug()
        resp = self.client.post(
            f"/{slug_before}/login/",
            {"username": "admin", "password": "pass1234"},
        )
        self.assertEqual(resp.status_code, 302)

        slug_after = get_current_slug()
        self.assertNotEqual(slug_after, slug_before)
