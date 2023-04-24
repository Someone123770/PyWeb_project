from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired

from The_proj.server import projectsphotos, projarchives


class PostProjForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    proj_type = SelectField('Тип', choices=['PyQt', 'pygame', 'WEB', 'Другое'], default=1)
    platform = StringField('Платформа')
    short_description = TextAreaField("Краткое описание")
    detailed_description = TextAreaField("Подробное описание")
    archive = FileField('Архив', validators=[FileAllowed(projarchives, 'Image only!'),
                                             FileRequired('File was empty!')])
    image = FileField('Обложка', validators=[FileAllowed(projectsphotos, 'Image only!'),
                                             FileRequired('File was empty!')])
    submit = SubmitField('Отправить проект')
