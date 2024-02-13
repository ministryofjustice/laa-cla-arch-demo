from form import CaseForm
from monolith_model import db, Case

from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import requests
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select

app = Flask(__name__)

# monolith only section
#
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monolith.sqlite3'
app.config['SECRET_KEY'] = 'random string'
db.init_app(app)
#
# end of monolith section

@app.route("/")
def hello_world():
    return """
<div><a href="monolith">monolith</a></div>
<div><a href="flask_and_drf">flask + DRF</a></div>
<div><a href="flask_and_fastapi">flask + FastAPI</a></div>
"""


@app.route("/monolith", methods=['GET', 'POST'])
def form1():
    form = CaseForm(request.form)
    case = db.session.scalars(db.select(Case).limit(1)).first()
    if request.method == 'POST' and form.validate():
        if not case:
            # create case
            case = Case(name=form.name.data)
            db.session.add(case)
        else:
            # amend existing case
            case.name = form.name.data
        db.session.commit()
        print('Saved!')
    elif case:
        form.name.data = case.name
    return render_template('form.html', form=form)

DRF_APP_BASE_URL = "http://localhost:5001"

@app.route("/flask_and_drf", methods=['GET', 'POST'])
def form2():
    form = CaseForm(request.form)
    case_response = requests.get(DRF_APP_BASE_URL + "/case")
    case_response.raise_for_status()
    case = case_response.json()
    if request.method == 'POST' and form.validate():
        if not case:
            # create case
            # case = Case(name=form.name.data)
            case = {"name": form.name.data}
            response = requests.post(DRF_APP_BASE_URL + "/case/", json=case)
            if response.status_code == 201:
                print('Saved!')
            else:
                raise requests.HTTPError(response.status_code)
        else:
            # amend existing case
            case.name = form.name.data
        db.session.commit()
        flash('Saved!')
    elif case:
        breakpoint()
        form.name.data = case.name
    return render_template('form.html', form=form)


@app.route("/flask_and_fastapi", methods=['GET', 'POST'])
def form3():
    return "<p>Hello, World!</p>"
