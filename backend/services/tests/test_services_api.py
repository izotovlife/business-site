import pytest
from services.models import Service


@pytest.mark.django_db
def test_services_list(client):
    Service.objects.create(slug="a", title="A", description="d", order=2)
    Service.objects.create(slug="b", title="B", description="d", order=1, is_active=False)
    Service.objects.create(slug="c", title="C", description="d", order=1)

    resp = client.get("/api/v1/services/")
    assert resp.status_code == 200
    data = resp.json()
    titles = [s["title"] for s in data]
    assert titles == ["C", "A"]
