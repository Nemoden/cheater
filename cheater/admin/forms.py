from wtforms import validators, Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField

class AddForm(Form):
  name = TextField("Name", validators = [validators.required()], description = u"Cheatsheet name")
  cheat = TextAreaField("Cheat", validators = [validators.required()], description = u"Cheatsheet")
  submit = SubmitField("Add", description = u"Create a cheatsheet")
  preview = SubmitField("Preview", description = u"Preview a cheatsheet")

class EditForm(Form):
  name = TextField("Name", validators = [validators.required()], description = u"Cheatsheet name")
  cheat = TextAreaField("Cheat", validators = [validators.required()], description = u"Cheatsheet")
  submit = SubmitField("Update", description = u"Update a cheatsheet")
  preview = SubmitField("Preview", description = u"Preview a cheatsheet")
