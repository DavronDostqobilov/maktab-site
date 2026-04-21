#!/bin/bash
# Deployment script for production

echo "📦 Dependencies o'rnatish..."
pip install -r requirements.txt

echo "🔧 Environment variables o'rnatish..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "⚠️  .env fayli yaratildi. Iltimos, sozlamalarni o'zgartirib oling!"
fi

echo "🗂️  Static fayllarni jamlash..."
python manage.py collectstatic --noinput

echo "🗄️  Database migratsiyalari..."
python manage.py migrate

echo "✅ Deployment tayyor! Server o'tkazuvini boshlash uchun:"
echo "   gunicorn config.wsgi:application --bind 0.0.0.0:8000"
