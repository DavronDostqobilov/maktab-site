#!/usr/bin/env bash
# Django Loyihasi Uchun Tezkor Komandalari

# 🟦 Local Development
echo "=== LOCAL DEVELOPMENT ===" 

# Virtual environment'ni faollash
# source venv/bin/activate

# Server ishga tushirish
alias runserver="python manage.py runserver"
alias runserver0="python manage.py runserver 0.0.0.0:8000"

# Database
alias migrate="python manage.py migrate"
alias makemigrations="python manage.py makemigrations"
alias migrations-status="python manage.py showmigrations"
alias superuser="python manage.py createsuperuser"

# Static files
alias collect-static="python manage.py collectstatic --noinput"
alias static-clear="python manage.py collectstatic --clear --noinput"

# Testing
alias test="python manage.py test"
alias check="python manage.py check"
alias shell="python manage.py shell"

# 🟩 Production Server
echo "=== PRODUCTION SERVER ===" 

# Gunicorn ishga tushirish
alias gunicorn-start="gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 4"

# Systemd
# sudo systemctl start maktab
# sudo systemctl stop maktab
# sudo systemctl restart maktab
# sudo systemctl status maktab
# sudo journalctl -u maktab -f

# 🔵 Environment Setup
echo "=== ENVIRONMENT SETUP ===" 

# Python virtual environment yaratish
# python3 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt

# .env yaratish
# cp .env.example .env

# 📊 Quick Commands
echo "=== QUICK COMMANDS ===" 

# Debug: Django version
alias django-version="python -c 'import django; print(django.get_version())'"

# Installed apps check
alias check-apps="python manage.py shell -c 'from django.apps import apps; print([app.name for app in apps.get_app_configs()])'"

# Database info
alias db-info="python manage.py dbshell"

# Flush database (WARN: Clear all data!)
# python manage.py flush --no-input

echo "✅ Aliases o'rnatildi!"
echo ""
echo "📝 Foydalanish:"
echo "  runserver          - Local server'da ishga tushirish"
echo "  migrate            - Database migratsiyalari"
echo "  makemigrations     - Yangi migratsiya yaratish"
echo "  superuser          - Admin user yaratish"
echo "  collect-static     - Static fayllarni jamlash"
echo "  gunicorn-start     - Production server'da ishga tushirish"
