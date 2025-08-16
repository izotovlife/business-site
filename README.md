# 🚀 Business Site (Django + React)

Полноценный сайт-визитка с админкой, защищённой динамическим URL, и современным API на основе **Django REST Framework**.  
Фронтенд построен на **React** с поддержкой адаптивной верстки.

---

## 📌 Основной функционал

### Backend (Django)
- Версияция API: все эндпоинты доступны по `/api/v1/`
- Эндпоинт для заявок `/api/v1/leads/`
- Поддержка **OpenAPI/Swagger/Redoc** (документация API)
- Динамический URL админки + honeypot для защиты
- Вынесение чувствительных данных в `.env`
- Настроены **CORS** и **CSRF**
- Поддержка **медиа/статики**
- Миграция с моделью `Lead`

### Frontend (React)
- Компоненты:
  - `Header`
  - `Footer`
  - `OrderModal`
- Подключён `Api.js` для работы с `/api/v1/`
- Обновлены страницы:
  - `Portfolio`
  - `Services`
  - `Testimonials`
- Адаптивные стили через `theme.css`

### Инфраструктура
- Подготовлен `requirements.txt` (backend)
- Обновлён `.gitignore` (venv, node_modules, build, SQLite, media, IDE)
- Минимизированы риски утечки ключей и конфиденциальных данных

---

## 🛠️ Технологии

- **Backend**: Django, Django REST Framework, drf-spectacular  
- **Frontend**: React, Axios  
- **База данных**: SQLite (локально, легко заменить на PostgreSQL)  
- **UI**: Адаптивные стили (CSS)  

---

## 🚀 Последнее обновление

### 🔒 Улучшена безопасность и структура проекта
- Добавлен пакет `django-admin-honeypot` для защиты от сканеров на `/admin/`
- Реализован **динамический URL админки** при каждом запуске
- Вынесены чувствительные данные в переменные окружения
- Настроен CORS и CSRF для локального фронтенда
- Добавлена интеграция с **drf-spectacular** (OpenAPI/Swagger/Redoc)
- Подготовлен `requirements.txt`
- Обновлён `.gitignore`
- Минимизированы риски утечки ключей и конфиденциальных данных

---

## 📦 Установка и запуск

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
