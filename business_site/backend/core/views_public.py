from django.http import JsonResponse

def root_json(_request):
    return JsonResponse({
        "name": "Business Site API",
        "version": "1.0.0",
        "docs": "/api/docs/",
        "endpoints": {
            "sections": "/api/v1/sections/",
            "portfolio": "/api/v1/portfolio/",
            "testimonials": "/api/v1/testimonials/"
        }
    })


def health_json(_request):
    return JsonResponse({"status": "ok"})

