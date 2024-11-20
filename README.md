# Planet-Discoverers
Website for uploading newly discovered exoplanets using Django web framework.

## Project setup:
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

## Features
- User-Friendly Interface: A simple and intuitive design for uploading and managing exoplanet discoveries.
- Image Uploads: Share images of the discovered exoplanets.
- Discovery Database: Keep track of all user-uploaded exoplanets with detailed information.

## Technologies Used
- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript
- Database: PostgreSQL
- File Upload: Django's File Handling and Media Features


Here’s the updated README with Windows-specific commands for the terminal:

Exoplanet Discoveries Platform 🌌
A web platform for amateur astronomers to showcase their discovered exoplanets. Users can upload information about their discoveries and share pictures of these fascinating celestial objects.

Table of Contents
Features
Technologies Used
Installation
Usage
Contributing
License
Acknowledgments
Features
User-Friendly Interface: A simple and intuitive design for uploading and managing exoplanet discoveries.
Image Uploads: Share images of the discovered exoplanets.
Discovery Database: Keep track of all user-uploaded exoplanets with detailed information.
Technologies Used
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Database: PostgreSQL
File Upload: Django's File Handling and Media Features
Installation
Clone the repository:

cmd
Copy code
git clone https://github.com/username/exoplanet-discovery-platform.git
cd exoplanet-discovery-platform
Set up a virtual environment and activate it:

cmd
Copy code
python -m venv venv
venv\Scripts\activate
Install dependencies:

cmd
Copy code
pip install -r requirements.txt
Apply database migrations:

cmd
Copy code
python manage.py migrate
Create a superuser:

cmd
Copy code
python manage.py createsuperuser
Run the server:

cmd
Copy code
python manage.py runserver
Open a web browser and visit http://127.0.0.1:8000 to access the platform.

## Usage
- Register/Login: Create an account or log in to start uploading.
- Add Discovery: Click on "Add Planet" and fill in the required details.
- Upload Images: Share pictures of your discoveries along with descriptions.
- Explore: View discoveries from other astronomers.

## License
- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
