#C:\Users\ASUS Vivobook\PycharmProjects\izotoff.ru\business_site\backend\core\models.py

from django.db import models


class ServiceSection(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    icon = models.CharField(max_length=64, blank=True, default="")

    class Meta:
        ordering = ["id"]
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

    def __str__(self):
        return self.title


class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    image = models.ImageField(upload_to="portfolio/", blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Портфолио (работа)"
        verbose_name_plural = "Портфолио (работы)"

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    author = models.CharField(max_length=255, default="Без имени")  # <-- добавили default
    role = models.CharField(max_length=255, blank=True, default="")
    text = models.TextField()
    avatar = models.ImageField(upload_to="testimonials/", blank=True, null=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.author} — {self.role or 'клиент'}"


class Lead(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)  # телефон/telegram/email
    message = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=64, blank=True, default="site")  # откуда заявка

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Лид"
        verbose_name_plural = "Лиды"

    def __str__(self):
        return f"{self.name} ({self.contact})"
