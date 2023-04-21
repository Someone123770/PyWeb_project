from flask import Flask, render_template, redirect

from models import db_session
from models.users import User
from forms.loginform import LoginForm
from forms.registerform import RegisterForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    print('start_index')
    # flag = int(input("Зарегистрирован ли пользователь?"))
    # url_to_img = input("Введите путь к аватарке")
    return render_template('index.html', flag=0)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', title='Авторизация', form=form)


# @app.route('/registration', methods=['GET', 'POST'])
# def reg():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         return redirect('/login')
#     return render_template('registration.html', title='регистрация', form=form)

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
            user_role=form.user_role.data,
            platform=form.platform.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('registration.html', title='Регистрация', form=form)


def main():
    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()
