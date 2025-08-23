from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Service, Lead
from .serializers import ServiceSerializer, LeadCreateSerializer


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


class LeadCreateView(generics.CreateAPIView):
    serializer_class = LeadCreateSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        ip = self.request.META.get("HTTP_X_FORWARDED_FOR") or self.request.META.get(
            "REMOTE_ADDR"
        )
        serializer.save(
            ip=ip, source=self.request.query_params.get("src", "site")
        )


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def health(_):
    return Response({"status": "ok"})
