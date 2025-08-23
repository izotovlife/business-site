from datetime import timedelta
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.utils.crypto import get_random_string
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import AdminLink


@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def create_admin_link(request):
    ip = request.META.get("HTTP_X_FORWARDED_FOR") or request.META.get("REMOTE_ADDR")
    now = timezone.now()
    last = AdminLink.objects.filter(issued_to_ip=ip).order_by("-expires_at").first()
    if last and now - (last.expires_at - timedelta(seconds=120)) < timedelta(seconds=30):
        return Response({"detail": "Too many requests"}, status=429)
    slug = get_random_string(32)
    expires = now + timedelta(seconds=120)
    AdminLink.objects.create(slug=slug, expires_at=expires, issued_to_ip=ip)
    return Response({"url": f"/{slug}/"})


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def use_admin_link(request, slug):
    ip = request.META.get("HTTP_X_FORWARDED_FOR") or request.META.get("REMOTE_ADDR")
    link = get_object_or_404(AdminLink, slug=slug)
    if not link.is_valid(ip):
        return redirect("/")
    link.is_active = False
    link.used_at = timezone.now()
    link.save(update_fields=["is_active", "used_at"])
    request.session["admin_gate_ok"] = True
    request.session.modified = True
    return redirect(settings.ADMIN_INTERNAL_PATH)
