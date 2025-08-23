from django.urls import path
from .views import ServiceListView, LeadCreateView, health

urlpatterns = [
    path("health/", health),
    path("services/", ServiceListView.as_view(), name="services-list"),
    path("leads/", LeadCreateView.as_view(), name="lead-create"),
]
