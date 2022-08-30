# django-jwt
https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html
pip install virtualenv
 <!-- virtualenv env
env\scripts\active -->

 python -m venv venv
 venv\Scripts\active
 pip install django

 django-admin startproject backend
 python manage.py startapp courses

cd backend

 python manage.py startapp base

 pip install djangorestframework

pip freeze > requirements.txt

winpty python manage.py createsuperuser

python manage.py sqlmigrate course 0001