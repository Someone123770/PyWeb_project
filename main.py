from flask import Flask, render_template, redirect
from forms.loginform import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
@app.route('/index')
def index():
    print('start_index')
    flag = int(input("Зарегистрирован ли пользователь?"))
    # url_to_img = input("Введите путь к аватарке")
    return render_template('base.html', flag=flag)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    print('start0')
    app.run(port=8888, host='127.0.0.1')
