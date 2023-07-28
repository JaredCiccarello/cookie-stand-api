# api-quick-start

Template Project for starting up CRUD API with Django Rest Framework

## Customization Steps

- DO NOT migrate yet
- add additional dependencies as needed
  - Re-export requirements.txt as needed
- change `cookie_stands` folder to the app name of your choice
- Search through entire code base for `CookieStand`,`cookie_stands` and `cookie_stands` to modify code to use your resource
  - `project/settings.py`
  - `project/urls.py`
  - App's files
    - `views.py`
    - `urls.py`
    - `admin.py`
    - `serializers.py`
    - `permissions.py`
  - "Front" files
    - if including a customer facing portion of the site then update/recreate:
      - `urls_front.py`
      - `views_front.py`
      - template files
      - Make sure to update project `urls.py` to add routes to the "front".
- Update CookieStandModel with fields you need
  - Make sure to update other modules that would be affected by Model customizations. E.g. serializers, tests, etc.
- Rename `project/.env.sample` to `.env` and update as needed
  - To generate secret key use `python3 -c "import secrets; print(secrets.token_urlsafe())"`
- Run makemigrations and migrate commands when ready.
- Run `python manage.py collectstatic`
  - This repository includes static assets in repository. If you are using a Content Delivery Network then remove `staticfiles` from repository.
- Optional: Update `api_tester.py`

## Database

**NOTE:** If you are using Postgres instead of SQLite then make sure to install `psycopg2-binary` and include in `requirements.txt`




Issues:
.env
no secret key




# Lab - Class 34
## Project: cookie-stand
## Author: Jared Ciccarello

# Feature Tasks and Requirements
## Features - Django
- Add JWT Authentication to your API.
- Install needed libraries in project configuration and/or site settings.
- Keep any pre-existing authentication so DRF Browsable API still usable.
- Install needed libraries in project configuration and/or site settings.
## Features - Docker
- Switch to using Gunicorn instead of Django’s built in development server.
- mind the number of workers to avoid sluggishness
- Warning You will run into styling issues when you switch over to Gunicorn.
- On Django side you’ll need to properly handle static files using Whitenoise
- Storage Options
- Your choice of SQLite or PostgreSQL
- Adjust docker-compose.yml so that data is persisted in a volume outside of container.
- These steps are different depending on whether SQLite or PostgreSQL is being used.

## Contributions
ChatGPT
Brandon Mizutani
Raven Robertson

## Setup
env sample used

## How to initialize/run your application
python manage.py runserver
docker compose up --build
runs at http://localhost:8000/api/v1/cookie-stand
## Libraries / Requirements

asgiref==3.7.2
attrs==23.1.0
certifi==2023.5.7
charset-normalizer==3.1.0
contourpy==1.1.0
coverage==7.2.7
cycler==0.11.0
Django==4.2.3
django-appconf==1.0.5
django-compressor==4.4
django-environ==0.10.0
djangorestframework==3.14.0
fonttools==4.40.0
gunicorn==21.2.0
idna==3.4
inflection==0.5.1
iniconfig==2.0.0
jsonschema==4.18.0
jsonschema-specifications==2023.6.1
kiwisolver==1.4.4
markdown-it-py==3.0.0
matplotlib==3.7.2
mdurl==0.1.2
numpy==1.25.1
openapi==1.1.0
packaging==23.1
Pillow==10.0.0
pluggy==1.2.0
psycopg2-binary==2.9.6
Pygments==2.15.1
pyparsing==3.0.9
PyQt5==5.15.9
PyQt5-Qt5==5.15.2
PyQt5-sip==12.12.1
pytest==7.4.0
pytest-cov==4.1.0
python-dateutil==2.8.2
pytz==2023.3
rcssmin==1.1.1
referencing==0.29.1
requests==2.31.0
rich==13.4.2
rjsmin==1.2.1
rpds-py==0.8.10
six==1.16.0
sqlparse==0.4.4
urllib3==2.0.3
whitenoise==6.5.0



## Tests
Built-in Django testing

python manage.py tests.py
