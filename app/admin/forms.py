from wtforms import Form, BooleanField, StringField, PasswordField, validators,TextField

class RegistrationForm(Form):
    name = StringField('', [validators.Length(min=4, max=25)])
    email = StringField('', [validators.Length(min=6, max=35),validators.Email()]) 
    password = PasswordField('', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.length(min=3,max=50)
    ])
    confirm = PasswordField('Repeat Password')
    
class LoginForm(Form):
    email = StringField('', [validators.Length(min=6, max=35),validators.Email()]) 
    password = PasswordField('', [
        validators.DataRequired(),validators.length(min=3,max=50)])
    