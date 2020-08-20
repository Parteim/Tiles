from flask import Blueprint, redirect, session, render_template, request, url_for, flash

from Users.moduls import db, User

MODULE_NAME = 'User'

app_user = Blueprint(MODULE_NAME, __name__)


def sig_up_data_validation(form):
    if User.query.filter(User.username == form['username']).first() \
            or User.query.filter(User.email == form['email']).first() \
            or form['password'] != form['confirm']:
        return False
    return True


@app_user.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST' and sig_up_data_validation(request.form):
        try:
            user = User(
                username=request.form['username'],
                email=request.form['email'],
                password=request.form['password'],
            )
            db.session.add(user)
            db.session.commit()
        except Exception:
            flash('message')
    return render_template('User/sign-up.html')


@app_user.route('/sign-in', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter(User.username == username).first()
        if user and user.check_password(password):
            session['username'] = username
            return redirect(url_for('wall'))
    return render_template('User/sign-in.html')


@app_user.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('User.sign_in'))
