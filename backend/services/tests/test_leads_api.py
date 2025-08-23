import pytest
from services.models import Service, Lead


@pytest.mark.django_db
def test_lead_create(client):
    service = Service.objects.create(slug="s", title="S", description="d")
    payload = {
        "name": "Ivan",
        "phone": "123",
        "service": service.id,
        "consent": True,
    }
    resp = client.post("/api/v1/leads/", payload)
    assert resp.status_code == 201
    assert Lead.objects.count() == 1


@pytest.mark.django_db
def test_lead_create_invalid(client):
    resp = client.post("/api/v1/leads/", {"name": "", "consent": False})
    assert resp.status_code == 400
