from django.contrib import admin
from .models import ServiceSection, PortfolioItem, Testimonial, Lead


@admin.register(ServiceSection)
class ServiceSectionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "icon")
    search_fields = ("title", "content")


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "link")
    search_fields = ("title", "description")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "role")
    search_fields = ("author", "text", "role")


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "contact", "source", "created_at")
    search_fields = ("name", "contact", "message", "source")
    list_filter = ("source", "created_at")
