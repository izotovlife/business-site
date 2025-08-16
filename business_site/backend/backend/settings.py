# backend/backend/settings.py
from pathlib import Path
import os

# === БАЗОВОЕ ===
BASE_DIR = Path(__file__).resolve().parent.parent

# Секреты читаем из окружения, на dev есть дефолт
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
DEBUG = os.getenv("DEBUG", "1") == "1"

# На dev — локальные хосты; на прод — читай ALLOWED_HOSTS из окружения
if DEBUG:
    ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
else:
    # Пример: ALLOWED_HOSTS="izotoff.ru,www.izotoff.ru"
    ALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS", "").split(",") if h.strip()]

# === ПРИЛОЖЕНИЯ ===
INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 3rd-party
    "corsheaders",
    "rest_framework",
    "drf_spectacular",

    # Local apps
    "core",
]

# === MIDDLEWARE ===
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # ← строго до CommonMiddleware
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

# Шаблоны нужны для админки (сайт рендерить не будем)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # без пользовательских шаблонов
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

# === БАЗА ДАННЫХ ===
# Dev: sqlite; Прод: можно переехать на Postgres (см. комментарии ниже)
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DB_NAME", BASE_DIR / "db.sqlite3"),
        # Для Postgres раскомментируй и задай в окружении:
        # "ENGINE": "django.db.backends.postgresql",
        # "NAME": os.getenv("DB_NAME", "app"),
        # "USER": os.getenv("DB_USER", "app"),
        # "PASSWORD": os.getenv("DB_PASSWORD", ""),
        # "HOST": os.getenv("DB_HOST", "127.0.0.1"),
        # "PORT": os.getenv("DB_PORT", "5432"),
    }
}

# === ПАРОЛИ ===
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# === ЛОКАЛИ ===
LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_TZ = True

# === СТАТИКА / МЕДИА ===
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"   # для collectstatic в проде

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# === DRF ===
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
}

# === CORS / CSRF ===
if DEBUG:
    # Удобно в dev: разрешаем все источники
    CORS_ALLOW_ALL_ORIGINS = True

    # Если используешь cookie/CSRF в браузере (админка/логин), доверь локальные фронты
    CSRF_TRUSTED_ORIGINS = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        # на случай Vite
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]
else:
    # В проде лучше белые списки из окружения
    def _env_list(name: str):
        return [x.strip() for x in os.getenv(name, "").split(",") if x.strip()]

    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOWED_ORIGINS = _env_list("CORS_ALLOWED_ORIGINS")  # напр. "https://izotoff.ru"
    CSRF_TRUSTED_ORIGINS = _env_list("CSRF_TRUSTED_ORIGINS")  # напр. "https://izotoff.ru"

# === OpenAPI (drf-spectacular) ===
SPECTACULAR_SETTINGS = {
    "TITLE": "Business Site API",
    "DESCRIPTION": "API для сайта услуг (разделы, портфолио, отзывы, лиды).",
    "VERSION": "1.0.0",
}

# === ПОЧТА ===
# Dev: вывод в консоль; Прод: переопредели EMAIL_BACKEND и креды из окружения
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "noreply@example.com")
NOTIFY_TO = os.getenv("NOTIFY_TO", "izotovlife@yandex.ru")

# Пример для прод-отправки через SMTP (задай переменные окружения и раскомментируй):
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.yandex.ru")
# EMAIL_PORT = int(os.getenv("EMAIL_PORT", "465"))
# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
# EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "0") == "1"
# EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL", "1") == "1"

# === БЕЗОПАСНОСТЬ (включится автоматически, когда DEBUG=0) ===
if not DEBUG:
    SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "1") == "1"
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS", "3600"))
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
    X_FRAME_OPTIONS = "DENY"

# === ЛОГИРОВАНИЕ (полезно на dev и прод) ===
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "[{levelname}] {name}: {message}", "style": "{"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simple"},
    },
    "root": {"handlers": ["console"], "level": LOG_LEVEL},
}
