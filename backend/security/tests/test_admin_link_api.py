import pytest
from datetime import timedelta
from django.utils import timezone
from security.models import AdminLink


@pytest.mark.django_db
def test_admin_link_flow(client, django_user_model, settings):
    admin = django_user_model.objects.create_superuser("admin", "a@example.com", "pass")
    client.force_login(admin)
    resp = client.post("/api/security/admin-link/")
    assert resp.status_code == 200
    url = resp.json()["url"]
    assert url.startswith("/")
    # first use works
    resp2 = client.get(url)
    assert resp2.status_code == 302
    # second use fails
    resp3 = client.get(url)
    assert resp3.status_code == 302
    assert resp3.headers["Location"] == "/"


@pytest.mark.django_db
def test_admin_link_denied_for_non_admin(client, django_user_model):
    user = django_user_model.objects.create_user("user", "u@example.com", "pass")
    client.force_login(user)
    resp = client.post("/api/security/admin-link/")
    assert resp.status_code == 403


@pytest.mark.django_db
def test_admin_link_ttl(client, django_user_model):
    admin = django_user_model.objects.create_superuser("admin", "a@example.com", "pass")
    AdminLink.objects.create(
        slug="test", issued_to_ip="127.0.0.1", expires_at=timezone.now() - timedelta(seconds=1)
    )
    resp = client.get("/test/")
    assert resp.status_code == 302  # redirected to home because expired
