# Frontend app

## Setup

```
cd frontend_app
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

Create the database table
```
flask shell
# now in the flask shell:
from monolith_model import db
db.create_all()
```

## Run

```
cd frontend_app
source venv/bin/activate
flask run --reload
```
Browse it: http://127.0.0.1:5000


# Django Rest Framework (DRF) app

This uses old versions of Python, Django, DRF etc to match cla_backend, because the aim is to understand that codebase with a simple version of it.

Docs:

* Django 1.8: https://docs.djangoproject.com/en/1.8/
* DRF 3.3.3: https://github.com/encode/django-rest-framework/blob/3.3.3/docs/index.md

## Setup

Ensure you have pyenv and python2 installed - follow: https://github.com/ministryofjustice/cla_backend/blob/master/VIRTUAL_ENV.md#pyenv-python2

Then:

```
cd drf_app
python --version
```

Ensure it reports Python 2.7.18. (This should pick up the version in .python-version. If it's not correct, check your pyenv shell setup.)

Then:

```
pip install --upgrade pip
pip install virtualenv
virtualenv -p python2.7 venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Create the database table:

```
python manage.py migrate
```

## Run

```
cd drf_app
source venv/bin/activate
./manage.py runserver 5001 --traceback
```
Browse it: http://127.0.0.1:5001
