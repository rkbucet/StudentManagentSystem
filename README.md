# StudentManagentSystem
Simple django project for CRUD operation using MySQL

# Make virtual environment for install packages, plugins and dependencies ...
mkvirtualenv env

# Activate virtual environment
workon env or env\scripts\activate

# installation
pip install -r requirements.txt

# Create Database 'StudentDb' in MySQL and paste the code in settings.py file(enter user and password according to your MySQL credentials) 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'StudentDb',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'admin',
        'PORT': 3306
    }
}

# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run server to view the Project
python manage.py runserver