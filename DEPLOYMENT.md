# Deployment Guide

This Django application is now configured for production deployment with the following features:

## Security Features ✅
- Environment-driven configuration
- WhiteNoise for static file serving
- HTTPS/SSL security settings
- CSRF protection
- HSTS headers
- Secure session cookies

## Production Setup

### 1. Environment Configuration

Copy `env.example` to `.env` and configure your production values:

```bash
cp env.example .env
# Edit .env with your production settings
```

**Required Environment Variables:**
- `DJANGO_SECRET_KEY` - Generate a new one at https://djecrety.ir/
- `DJANGO_DEBUG=False` - NEVER set to True in production
- `DJANGO_ALLOWED_HOSTS` - Your domain(s), comma-separated
- `DATABASE_URL` - Your database connection string

**Optional Security Variables:**
- `DJANGO_SECURE_SSL_REDIRECT=True` - Redirect HTTP to HTTPS
- `DJANGO_SESSION_COOKIE_SECURE=True` - Secure session cookies
- `DJANGO_CSRF_COOKIE_SECURE=True` - Secure CSRF cookies
- `DJANGO_SECURE_HSTS_SECONDS=31536000` - HSTS max age
- `DJANGO_CSRF_TRUSTED_ORIGINS` - Trusted origins for CSRF

### 2. Database Setup

**PostgreSQL (Recommended):**
```bash
# Install PostgreSQL and create database
DATABASE_URL=postgresql://username:password@localhost:5432/myproject_db
```

**MySQL:**
```bash
DATABASE_URL=mysql://username:password@localhost:3306/myproject_db
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare for Production

```bash
# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create superuser
python manage.py createsuperuser
```

### 5. Run with Gunicorn

```bash
# Using the provided configuration
gunicorn -c gunicorn.conf.py myproject.wsgi:application

# Or manually
gunicorn --bind 0.0.0.0:8000 --workers 2 myproject.wsgi:application
```

## Platform-Specific Deployment

### Heroku
1. Add `Procfile`:
   ```
   web: gunicorn myproject.wsgi:application
   release: python manage.py migrate
   ```
2. Set environment variables in Heroku dashboard
3. Add PostgreSQL addon: `heroku addons:create heroku-postgresql:mini`

### Railway/Render
1. Connect your GitHub repository
2. Set environment variables in dashboard
3. Deploy automatically on git push

### VPS/DigitalOcean
1. Install Python, PostgreSQL, Nginx
2. Set up systemd service for gunicorn
3. Configure Nginx as reverse proxy
4. Set up SSL with Let's Encrypt

## Security Checklist

Before deploying:
- [ ] `DJANGO_DEBUG=False`
- [ ] Strong `DJANGO_SECRET_KEY` (50+ characters)
- [ ] Proper `DJANGO_ALLOWED_HOSTS`
- [ ] Database configured (not SQLite)
- [ ] SSL/HTTPS enabled
- [ ] Environment variables secured
- [ ] Run `python manage.py check --deploy`

## Local Development

For local development, the app uses SQLite and relaxed security settings. Just run:

```bash
python manage.py runserver
```

## Troubleshooting

**Static files not loading:**
- Run `python manage.py collectstatic`
- Check `STATIC_ROOT` and `STATIC_URL` settings

**Database connection errors:**
- Verify `DATABASE_URL` format
- Ensure database exists and user has permissions

**ALLOWED_HOSTS errors:**
- Add your domain to `DJANGO_ALLOWED_HOSTS`
- Include both www and non-www versions
