# Frontend

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
