from rest_framework.routers import DefaultRouter
from .views import (
    ServiceSectionViewSet,
    PortfolioItemViewSet,
    TestimonialViewSet,
    LeadViewSet,
)

router = DefaultRouter()
router.register(r"sections", ServiceSectionViewSet, basename="section")
router.register(r"portfolio", PortfolioItemViewSet, basename="portfolio")
router.register(r"testimonials", TestimonialViewSet, basename="testimonial")
router.register(r"leads", LeadViewSet, basename="lead")  # только POST

# ВАЖНО: именно router.urls, а не include(router)
urlpatterns = router.urls

