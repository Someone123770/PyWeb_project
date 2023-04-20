from flask import Flask, render_template, redirect

from Cave_of_projects.forms.RegForm import RegisterForm
from Cave_of_projects.forms.login_form import LoginForm
from Cave_of_projects.handlers import register_api
from Cave_of_projects.models.users import User
from models import db_session
from flask_login import LoginManager, login_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


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


@app.route("/")
def index():
    return render_template("base.html", flag=0)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        print('1')
        user = User(
            user_name=form.name.data,
            email=form.email.data,
            # about=form.about.data,
            user_role=form.user_role.data,
            platform=form.platform.data
        )
        print('ok')
        user.set_password(form.password.data)
        print('ok')
        db_sess.add(user)
        print('ok')
        db_sess.commit()
        print('ok')
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(register_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()
