from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_ast = StringField('Astronaut id', validators=[DataRequired()])
    password_ast = PasswordField('Password', validators=[DataRequired()])
    id_cap = StringField('Cap id', validators=[DataRequired()])
    password_cap = PasswordField('Cap password', validators=[DataRequired()])
    submit = SubmitField('Войти')