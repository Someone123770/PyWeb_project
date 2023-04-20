from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    title = 'Site'
    print('start_index')
    return render_template('login.html', title=title)


if __name__ == '__main__':
    print('start0')
    app.run(port=8888, host='127.0.0.1')
