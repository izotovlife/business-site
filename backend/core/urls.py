from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceSectionViewSet

router = DefaultRouter()
router.register('sections', ServiceSectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
