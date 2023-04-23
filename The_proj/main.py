import os

from flask import Flask, render_template, redirect
from flask_login import current_user, LoginManager, login_user, login_required, logout_user
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class, ARCHIVES

from models import db_session
from models.users import User
from forms.loginform import LoginForm
from forms.registerform import RegisterForm

from constants.constants import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

# """ for uploading """
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['UPLOADED_PROJECTSPHOTOS_DEST'] = os.path.join(basedir, 'static/uploads')

projectsphotos = UploadSet('projectsphotos', IMAGES)
configure_uploads(app, projectsphotos)
# максимальный размер файла, по умолчанию 16MB
patch_request_class(app)


# IDK why it doesn't work, but further I'll change that (the path remains general)
app.config['UPLOADED_PROJARCHIVES_DEST'] = os.path.join(basedir, 'static/archives')
#

projarchives = UploadSet('projectsphotos', ARCHIVES)
configure_uploads(app, projarchives)
patch_request_class(app)
# """ for uploading """


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
@app.route('/index')
def index():
    if current_user.is_authenticated:
        user = load_user(current_user.get_id())
        fl = user.role
    else:
        fl = 0
    return render_template('index.html', flag=fl)


@app.route('/post-project', methods=['GET', 'POST'])
def post_project():

    from The_proj.models.projects import Project
    from The_proj.models.users import User  # THAT'S ESSENTIAL
    from forms.post_proj_form import PostProjForm

    form = PostProjForm()
    if form.validate_on_submit():
        # saving in /static/...
        filename_image = projectsphotos.save(form.image.data)
        filename_archive = projarchives.save(form.archive.data)

        db_sess = db_session.create_session()
        proj = Project(
            project_name=form.name.data,
            project_type=PROJECTS_TYPES[form.proj_type.data],
            project_platform=form.platform.data,
            short_description=form.short_description.data,
            description=form.detailed_description.data,
            archive=filename_archive,
            image=filename_image
        )
        db_sess.add(proj)
        db_sess.commit()
        return redirect('/')
    return render_template('post_project.html', title='Выложить проект', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.confirm_password.data:
            return render_template('registration.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('registration.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            user_name=form.name.data,
            email=form.email.data,
            about=form.about.data,
            user_role=USERS_TYPES[form.user_role.data],
            platform=form.platform.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        login_user(user)
        return redirect('/index')
    return render_template('registration.html', title='Регистрация', form=form)


def main():
    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()
