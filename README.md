# Whatsbyte Healthcare Backend Assignment

A Django REST API for managing patients, doctors, and their mappings, using Neon Serverless Postgres, JWT authentication, and Swagger docs.

## Features
- Register/login users with JWT (`/api/auth/register/`, `/api/auth/login/`).
- CRUD for patients (`/api/patients/`) and doctors (`/api/doctors/`).
- Assign/delete patient-doctor mappings (`/api/mappings/`).
- Swagger docs at `/api/docs/`.
- Secure with rate limiting and production settings.
- Neon Postgres for scalable database.
- Dockerized with Gunicorn.

## Tech Stack
- Django 5.1.1, Django REST Framework 3.15.2
- Neon Postgres (PostgreSQL 14+)
- SimpleJWT 5.3.1, drf-spectacular 0.27.2
- Gunicorn 23.0.0, Whitenoise 6.6.0
- Python 3.10+, Docker

## Setup

### Prerequisites
- Python 3.10+ ([python.org](https://www.python.org/downloads/))
- Neon account ([neon.tech](https://neon.tech))
- Docker ([docker.com](https://www.docker.com/get-started)) (optional)

### 1. Clone Project
```bash
git clone <your-repo-url>
cd healthcare_backend
```

### 2. Set Up Neon
1. Log in to [Neon Console](https://console.neon.tech).

2. Create a project, get connection string from **Dashboard > Connect > Django** (e.g., `postgresql://user:password@ep-your-host.region.aws.neon.tech/dbname?sslmode=require`).

3. Copy `.env.example` to `.env` and fill:
   ```bash
   cp .env.example .env
   ```
   Edit `.env`:
   ```
   DB_NAME=your_neon_db
   DB_USER=your_neon_user
   DB_PASSWORD=your_neon_password
   DB_HOST=ep-your-host.region.aws.neon.tech
   DB_PORT=5432
   SECRET_KEY=your_secret_key  # Run: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ALLOWED_HOSTS=localhost,127.0.0.1
   DJANGO_SETTINGS_MODULE=config.settings.prod || config.settings.dev
   ```


### 3. Local Setup
1. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py makemigrations core
   python manage.py migrate
   ```
4. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Start server:
   ```bash
   python manage.py runserver
   ```
   - Access: `http://localhost:8000`
   - Swagger: `http://localhost:8000/api/docs/`
   - Admin: `http://localhost:8000/admin/`

### 4. Docker Setup
1. Ensure `.env` has Neon credentials.

2. Build and run:
   ```bash
   docker-compose up --build
   ```

3. Run migrations:
   ```bash
   docker-compose exec web python manage.py makemigrations core
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser
   ```
4. Access: `http://localhost:8000`
5. Stop: `docker-compose down`


### 5. Test APIs
- **Locally**:
  - Register: `curl -X POST http://localhost:8000/api/auth/register/ -d '{"name": "Test", "email": "test@example.com", "password": "pass123"}'`

  - Login: `curl -X POST http://localhost:8000/api/auth/login/ -d '{"email": "test@example.com", "password": "pass123"}'` (get token)

  - Use token: `curl -H "Authorization: Bearer <token>" http://localhost:8000/api/patients/`
- **Live**:
  - Register: `curl -X POST https://whatsbyte.onrender.com/api/auth/register/ -d '{"name": "Test", "email": "test@example.com", "password": "pass123"}'`

  - Login: `curl -X POST https://whatsbyte.onrender.com/api/auth/login/ -d '{"email": "test@example.com", "password": "pass123"}'`

  - Use token: `curl -H "Authorization: Bearer <token>" https://whatsbyte.onrender.com/api/patients/`

  - Try Swagger For UI Documentation Based Live Testing: [https://whatsbyte.onrender.com/api/docs/](https://whatsbyte.onrender.com/api/docs/)

### 6. Run Tests
```bash
python manage.py test core
```

### Troubleshooting
- **HTTPS Error**: Use `http://localhost:8000` (dev server doesn’t support HTTPS).
- **Neon Connection**: Verify credentials in `.env`. Test with `psql`. Check Neon Console for compute status.
- **Logs**: See `logs/django.log` or `docker-compose logs web`.
- **Delete Issues**: Ensure correct `DELETE` method and valid token for `/api/mappings/<id>/`.

### Production Notes
- Use `config.settings.prod` (set `DJANGO_SETTINGS_MODULE=config.settings.prod`).
- Deploy with Nginx and HTTPS.
- Use Neon’s connection pooling for high traffic.
- Store media in S3 with `django-storages`.


#### Thanks for Reading so far ❤️
