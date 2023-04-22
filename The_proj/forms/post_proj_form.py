from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired


class PostProjForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    proj_type = SelectField('Тип', choices=['PyQt', 'pygame', 'WEB', 'Другое'], default=1)
    platform = StringField('Платформа')
    short_description = TextAreaField("Краткое описание")
    detailed_description = TextAreaField("Подробное описание")
    archive = FileField('Архив')
    image = FileField('Обложка')
    submit = SubmitField('Отправить проект')
