from flask import render_template, redirect

from Cave_of_projects.forms.RegForm import RegisterForm
from Cave_of_projects.main import app
from Cave_of_projects.models import db_session
from Cave_of_projects.models.users import User


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
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data,
            user_role=form.user_role.data,
            platform=form.platform.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')  # prolly not login
    return render_template('register.html', title='Регистрация', form=form)
