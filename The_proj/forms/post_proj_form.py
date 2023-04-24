from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired

from main import projectsphotos, projarchives
from constants import PROJECTS_TYPES


class PostProjForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    proj_type = SelectField('Тип', choices=list(PROJECTS_TYPES.keys()), default=1)
    platform = StringField('Платформа', validators=[DataRequired()])
    short_description = TextAreaField("Краткое описание")
    detailed_description = TextAreaField("Подробное описание")
    archive = FileField('Архив', validators=[FileAllowed(projarchives, 'Archives only!'),
                                             FileRequired('File was empty!')])
    image = FileField('Обложка', validators=[FileAllowed(projectsphotos, 'Image only!')])
    submit = SubmitField('Отправить проект')
