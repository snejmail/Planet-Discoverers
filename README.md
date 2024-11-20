# Planet-Discoverers
Website for uploading newly discovered exoplanets using Django web framework.

Project setup:
1. Clone the repo:
  git clone https:/github.com/snejmail/Planet-Discoverers
  cd Planet-Discoverers

3. Set up a virtual environment and activate it:
  python -m venv venv
  venv\Scripts\activate

5. Install dependencies:
  pip install -r requirements.txt

4. Change DB settings in settings.py
  DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.postgresql",
          "NAME": "your_db_name",
          "USER": "your_username",
          "PASSWORD": "your_pass",
          "HOST": "127.0.0.1",
          "PORT": "5432",
      }
  }

5. Apply database migrations:
  python manage.py migrate

6. Create a superuser:
  python manage.py createsuperuser

7. Run the project:
  python manage.py runserver
