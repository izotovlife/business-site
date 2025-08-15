# core/models.py
from django.db import models

class ServiceSection(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    icon = models.CharField(max_length=100, blank=True, help_text="CSS-класс или ссылка на иконку")

    def __str__(self):
        return self.title

class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    avatar = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name
