# Назначение: тесты middleware динамического slug; path: backend/security/tests/test_middleware_rewrite.py.
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

import pytest
from django.conf import settings

from security.utils import rotate_slug


@pytest.mark.django_db
def test_middleware_rewrite(client):
    slug = rotate_slug()
    resp = client.get(f"/{slug}/", follow=True)
    assert resp.status_code == 200
    assert any(t.name == "admin/login.html" for t in resp.templates)

    resp2 = client.get(settings.ADMIN_INTERNAL_PATH)
    assert resp2.status_code == 404
