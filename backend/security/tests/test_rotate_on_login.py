# Назначение: проверка ротации slug при логине; path: backend/security/tests/test_rotate_on_login.py.
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

import pytest
from django.contrib.auth import get_user_model

from security.utils import rotate_slug, get_current_slug


@pytest.mark.django_db
def test_rotate_on_login(client):
    User = get_user_model()
    User.objects.create_superuser("admin", "a@example.com", "pass")
    slug_before = rotate_slug()
    resp = client.post(f"/{slug_before}/login/", {"username": "admin", "password": "pass"}, follow=True)
    assert resp.status_code == 200
    slug_after = get_current_slug()
    assert slug_after != slug_before
