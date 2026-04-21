# 🚀 Django Loyihasi Serverga Yuklash Qo'llanmasi

## ✅ Pre-Deployment Tekshiruvi

### 1. **Environment Variables**
- [ ] `.env` faylini yaratish: `cp .env.example .env`
- [ ] `SECRET_KEY` o'zgartirib, yangi kalit yaratish
- [ ] `DEBUG=False` o'rnatish
- [ ] `ALLOWED_HOSTS` = `narpayim.uz,www.narpayim.uz` ✅ Sozlandi

### 2. **Dependencies**
- [ ] `requirements.txt` mavjudmi? ✅ Yaratilgan
- [ ] Barcha dependencies o'rnatilganmi?
  ```bash
  pip install -r requirements.txt
  ```

### 3. **Database**
- [ ] Migratsiyalar qo'llanilganmi?
  ```bash
  python manage.py migrate
  ```
- [ ] Super foydalanuvchi yaratilganmi?
  ```bash
  python manage.py createsuperuser
  ```

### 4. **Static Files**
- [ ] Static fayllar jamlangumi?
  ```bash
  python manage.py collectstatic --noinput
  ```

### 5. **Security**
- [ ] DEBUG = False ✅ Sozlandi
- [ ] ALLOWED_HOSTS belgilandi ✅ Sozlandi
- [ ] SECRET_KEY o'zgartirildi ✅ Environment'dan o'qiladi
- [ ] HTTPS/SSL sertifikat ✅ Settings'da sozlandi
- [ ] CSRF protection ✅ Mavjud

## 🔧 Server Setup (Linux/Ubuntu)

### Python & Virtual Environment
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Web Server (Nginx)
```bash
sudo apt-get install nginx
```

### Application Server (Gunicorn)
```bash
# requirements.txt'da mavjud
pip install gunicorn
```

### Database (PostgreSQL - ixtiyoriy)
```bash
sudo apt-get install postgresql postgresql-contrib
```

## 🚀 Deployment Qadam-bo'yicha

### 1. Server'da setup
```bash
git clone <repository-url>
cd maktab-site
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# .env'ni tahrirlash
```

### 2. Database migratsiyalari
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 3. Static files
```bash
python manage.py collectstatic --noinput
```

### 4. Gunicorn test
```bash
gunicorn config.wsgi:application --bind 127.0.0.1:8000
```

### 5. Systemd Service (production uchun)
`/etc/systemd/system/maktab.service` yaratish:
```ini
[Unit]
Description=Maktab Site Gunicorn App
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/maktab-site
ExecStart=/path/to/maktab-site/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:8000 config.wsgi:application
Restart=always

[Install]
WantedBy=multi-user.target
```

### 6. Nginx Configuration
`/etc/nginx/sites-available/maktab` yaratish:
```nginx
server {
    listen 80;
    server_name narpayim.uz www.narpayim.uz;

    location /static/ {
        alias /path/to/maktab-site/staticfiles/;
    }

    location /media/ {
        alias /path/to/maktab-site/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

## 🔒 SSL Certificate (HTTPS)
```bash
sudo apt-get install certbot python3-certbot-nginx
sudo certbot --nginx -d narpayim.uz -d www.narpayim.uz
```

## 📊 Monitoring & Logs
```bash
# Gunicorn logs
sudo journalctl -u maktab -f

# Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

## ⚠️ Jiddiy Soatlar

- [ ] DEBUG = False
- [ ] SECRET_KEY private
- [ ] ALLOWED_HOSTS to'g'ri
- [ ] Database backup plan
- [ ] Media files backup
- [ ] Monitoring/Logging setup
- [ ] SSL/HTTPS enabled

## 🆘 Agar muammo bo'lsa

1. Logs'ni tekshirish: `python manage.py shell`
2. Migratsiyalarni tekshirish: `python manage.py showmigrations`
3. Static files: `python manage.py collectstatic --clear --noinput`
