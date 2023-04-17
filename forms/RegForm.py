from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    about = TextAreaField("Немного о себе")
    user_role = SelectField('Кто вы?', choices=['Первокурсник ЛАЯ', 'Второкурсник ЛАЯ',
                                                'Учитель ЛАЯ', 'Другое'], default=0)
    platform = StringField('Платформа обучающегося')
    submit = SubmitField('Войти')
