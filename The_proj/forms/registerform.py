from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField, TextAreaField, SelectField
from wtforms.validators import DataRequired, InputRequired, EqualTo

from constants import USERS_TYPES

class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', [InputRequired(), EqualTo('confirm_password', message='Пароли должны совпадать')])
    confirm_password = PasswordField('Повторите пароль')
    name = StringField('Имя пользователя', validators=[DataRequired()])
    about = TextAreaField("Немного о себе")
    user_role = SelectField('Кто вы?', choices=list(USERS_TYPES.keys()), default=0)
    platform = StringField('Платформа обучающегося')
    submit = SubmitField('Зарегистрироваться')
