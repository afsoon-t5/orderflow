# معماری پیشنهادی نسخه تجاری

Frontend/Panel -> FastAPI -> PostgreSQL
                         -> Redis/Celery برای کارهای زمان‌بندی‌شده
                         -> Telegram Bot API برای اعلان‌ها

نسخه دمو از SQLite و پردازش داخل FastAPI استفاده می‌کند تا بدون سرویس جانبی اجرا شود.
نسخه تجاری می‌تواند احراز هویت، RBAC، PostgreSQL، Redis/Celery، لاگ، Docker و استقرار روی VPS داشته باشد.
