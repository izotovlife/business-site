# Назначение: тест API получения ссылки админки; path: backend/security/tests/test_admin_link_api.py.
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

import pytest
from django.contrib.auth import get_user_model

from security.utils import rotate_slug


@pytest.mark.django_db
def test_admin_link_api(client):
    User = get_user_model()
    admin = User.objects.create_superuser("admin", "a@example.com", "pass")
    user = User.objects.create_user("user", "u@example.com", "pass")
    slug = rotate_slug()

    client.force_login(admin)
    resp = client.get("/api/admin-link")
    assert resp.status_code == 200
    assert resp.json()["admin_url"] == f"/{slug}/"
    client.logout()

    client.force_login(user)
    resp2 = client.get("/api/admin-link")
    assert resp2.status_code == 403
