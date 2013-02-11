from wtforms import validators, Form
from wtforms import TextField, SubmitField, PasswordField


class LoginForm(Form):
    username = TextField("Username", validators=[validators.required()],
                         description=u"Login")
    password = PasswordField("Password", validators=[validators.required()],
                             description=u"Cheatsheet")
    submit = SubmitField("Login", description=u"Login button")
