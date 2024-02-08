from wtforms import Form, StringField


class CaseForm(Form):
    name = StringField('Name')
