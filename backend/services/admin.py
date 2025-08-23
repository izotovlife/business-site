from django.contrib import admin
from .models import Service, Lead


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "price_from", "order")
    list_editable = ("is_active", "price_from", "order")
    search_fields = ("title", "short", "description")


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "name",
        "phone",
        "email",
        "service",
        "status",
        "source",
        "ip",
    )
    list_filter = ("status", "source", "service")
    search_fields = ("name", "phone", "email", "message")
    readonly_fields = ("created_at", "ip", "source")
