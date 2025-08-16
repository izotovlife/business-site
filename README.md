# 🚀 Business Site (Django + React)

Полноценный сайт-визитка с админкой, защищённой динамическим URL, и современным API на основе **Django REST Framework**.

---

## 🔧 Стек технологий
- **Backend**: Django 5, DRF, drf-spectacular (Swagger, OpenAPI, Redoc)
- **Frontend**: React 18 + Material UI
- **База данных**: SQLite (по умолчанию) или PostgreSQL
- **Безопасность**:
  - `django-admin-honeypot` — ловушка для сканеров на `/admin/`
  - динамический URL админки (генерируется при каждом запуске)
  - вынесение ключей и паролей в `.env`
- **Прочее**:
  - CORS/CSRF защита
  - Pillow (для работы с изображениями)

---

## ⚙️ Установка и запуск

### 1. Клонирование проекта
```bash
git clone https://github.com/izotovlife/business-site.git
cd business-site
