from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, TextAreaField, SelectField, TextAreaField
from wtforms.validators import DataRequired, InputRequired


class PostProject(FlaskForm):
    project_name = StringField('Название проекта', validators=[DataRequired()])
    description = TextAreaField('Описание проекта', validators=[DataRequired()])
    about = TextAreaField("Немного о себе")
    user_role = SelectField('Кто вы?', choices=['Поступающий', 'Первокурсник ЛАЯ', 'Второкурсник ЛАЯ',
                                                'Учитель ЛАЯ', 'Другое'], default=0)
    platform = StringField('Платформа обучающегося')
    submit = SubmitField('Зарегистрироваться')
