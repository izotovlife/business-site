from django.db import models


class Service(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    short = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    price_from = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title


class Lead(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=32, blank=True)
    service = models.ForeignKey(Service, null=True, blank=True, on_delete=models.SET_NULL)
    message = models.TextField(blank=True)
    source = models.CharField(max_length=64, default="site")
    ip = models.GenericIPAddressField(null=True, blank=True)
    consent = models.BooleanField(default=False)
    status = models.CharField(
        max_length=16,
        default="new",
        choices=[("new", "Новая"), ("in_progress", "В работе"), ("done", "Сделано")],
    )

    def __str__(self):
        return f"{self.name} — {self.service.title if self.service else 'Без услуги'}"
