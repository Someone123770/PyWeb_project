from flask import Flask, render_template, redirect
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

@app.route('/registration', methods=['GET', 'POST'])
def reg():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect('/login')
    return render_template('registration.html', title='регистрация', form=form)


if __name__ == '__main__':
    print('start0')
    app.run(port=8888, host='127.0.0.1')
