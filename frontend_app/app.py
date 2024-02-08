from form import CaseForm
from monolith_model import db, Case

from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
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
    if request.method == 'POST' and form.validate():
        case = Case(name=form.name.data)
        db.session.add(case)
        db.session.commit()
        flash('Saved!')
    else:
        case = db.session.execute(db.select(Case)).first()
        if case:
            form.name.data = case[0].name
    return render_template('form.html', form=form)

@app.route("/flask_and_drf")
def form2():
    return "<p>Hello, World!</p>"


@app.route("/flask_and_fastapi")
def form3():
    return "<p>Hello, World!</p>"
