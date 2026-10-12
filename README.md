# OrderFlow — Python / FastAPI Portfolio Demo

یک سیستم مدیریت سفارش و داشبورد فروش با Python و FastAPI.

🔗 **Live Demo:** https://orderflow.de2.netrun.io

## ✨ Features

- داشبورد مدیریت سفارشات
- ثبت سفارش جدید
- تغییر وضعیت سفارش
- گزارش فروش
- نمایش آمار سفارش‌ها
- REST API
- مستندات API با Swagger
- رابط کاربری فارسی و RTL
- SQLite database
- Docker support

## 🛠 Tech Stack

- Python
- FastAPI
- SQLite
- Jinja2
- HTML / CSS
- Docker
- REST API

## 📊 Dashboard

داشبورد شامل موارد زیر است:

- تعداد کل سفارش‌ها
- سفارش‌های جدید
- سفارش‌های در حال پردازش
- سفارش‌های تکمیل‌شده
- مجموع فروش
- جدول سفارش‌ها

## 🔌 API

مستندات تعاملی API:

`/docs`

API اصلی:

`/api/orders`

Health Check:

`/health`

## 🚀 Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
