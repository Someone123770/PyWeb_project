from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    print('start_index')
    flag = int(input("Зарегистрирован ли пользователь?"))
    # url_to_img = input("Введите путь к аватарке")
    return render_template('base.html', flag=flag)


if __name__ == '__main__':
    print('start0')
    app.run(port=8888, host='127.0.0.1')
