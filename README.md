# Planet-Discoverers
Website for uploading newly discovered exoplanets using the Django web framework.

## Project Setup
- **Clone the repo:**  
    ```bash
    git clone https://github.com/snejmail/Planet-Discoverers  
    cd Planet-Discoverers  
    ```

- **Set up a virtual environment and activate it:**  
    ```bash
    python -m venv venv  
    venv\Scripts\activate  
    ```

- **Install dependencies:**  
    ```bash
    pip install -r requirements.txt  
    ```

- **Change DB settings in `settings.py`:**  
    ```python
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
    ```

- **Apply database migrations:**  
    ```bash
    python manage.py migrate  
    ```

- **Create a superuser:**  
    ```bash
    python manage.py createsuperuser  
    ```

- **Run the project:**  
    ```bash
    python manage.py runserver  
    ```

## Features
- **User-Friendly Interface:** A simple and intuitive design for uploading and managing exoplanet discoveries.
- **Image Uploads:** Share images of the discovered exoplanets.
- **Discovery Database:** Keep track of all user-uploaded exoplanets with detailed information.

## Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** PostgreSQL
- **File Upload:** Django's File Handling and Media Features

## Usage
- **Register/Login:** Create an account or log in to start uploading.
- **Add Discovery:** Click on "Add Planet" and fill in the required details.
- **Upload Images:** Share pictures of your discoveries along with descriptions.
- **Explore:** View discoveries from other astronomers.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
