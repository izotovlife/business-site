from django.db import migrations


SERVICES = [
    ("dzen-management", "Ведение Дзен-каналов."),
    ("smm", "Ведение VK/OK/Telegram."),
    ("content-photo-video", "Обработка фото/монтаж видео."),
    ("reviews-reply", "Ответы на отзывы (OTVETO / MPSTATS)."),
    ("whatsapp-business", "Настройка WhatsApp Business."),
    ("marketplaces-support", "Поддержка товаров/описаний."),
    ("site-admin", "Администрирование сайтов (WordPress/Битрикс)."),
    ("seo-content", "SEO-тексты/фиды."),
    ("b2b-orders", "Приём и сопровождение B2B-заказов."),
]


def seed_services(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    for order, (slug, title) in enumerate(SERVICES):
        Service.objects.create(slug=slug, title=title, description=title, order=order)


def unseed_services(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    Service.objects.filter(slug__in=[s[0] for s in SERVICES]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [migrations.RunPython(seed_services, unseed_services)]
