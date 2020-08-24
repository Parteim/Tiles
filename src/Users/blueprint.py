from flask import Blueprint, redirect, session, render_template, request, url_for, flash, g
from flask.views import View, MethodView
from flask_login import current_user, login_user, logout_user, login_required
from email_validator import validate_email, EmailSyntaxError

from Users.models import db, User, Profile

from app import login_manager

MODULE_NAME = 'User'

app_user = Blueprint(MODULE_NAME, __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def load_user():
    return redirect(url_for('User.sign-in', next=request.endpoint))


@app_user.before_request
def get_current_user():
    g.user = current_user


class SignUp(MethodView):
    def __init__(self):
        self.template = 'User/sign-up.html'
        self.form = request.form
        self.title = 'Sign up'
        self.symbols = ['*', '!', '@', '#', '$', '%', '^', '&', '_', '-', '=', '+']
        self.password_len = 6

    def sig_up_data_validation(self):
        def check_symbols():

            for symbol in self.symbols:
                if symbol in password:
                    return True
            flash('Password must contain some of symbol \n' + ' '.join(self.symbols))
            return False

        flag = True

        email = self.form['email']
        password = self.form['password']
        confirm = self.form['confirm']
        try:
            validate_email(email).email
        except EmailSyntaxError:
            flash('Incorrect email.')
            flag = False
        if User.query.filter(User.email == email).first():
            flash('User with same email already exist.')
            flag = False
        if len(password) < self.password_len:
            flash(f'password must be much than {self.password_len}.')
            flag = False
        if not check_symbols():
            flag = False
        if password != confirm:
            flash('Password not confirmed.')
            flag = False
        return flag

    def get(self):
        return render_template(self.template, title=self.title)

    def post(self):
        if not self.sig_up_data_validation():
            return render_template(self.template)
        try:
            user = User(
                username=request.form['username'],
                email=request.form['email'],
                password=request.form['password'],
            )
            user_profile = Profile(user=user)
            db.session.add_all([user, user_profile])
            db.session.commit()
            flash('Sign up is successful.')
            return redirect(url_for('User.sign-in'))
        except Exception:
            flash('Something wrong')
        return redirect(url_for('User.sign-up'))


class SignIn(MethodView):
    def __init__(self):
        self.template = 'User/sign-in.html'
        self.title = 'Sign in'

    def get(self):
        return render_template(self.template, title=self.title)

    def post(self):
        email = request.form['email']
        password = request.form['password']
        try:
            next = url_for(request.args.get('next'))
        except TypeError:
            next = None
        user = User.query.filter(User.email == email).first()
        if user and user.check_password(password):
            login_user(user)
            flash(f'Welcome {user.username}')
        else:
            flash('Incorrect username or password.')
            return redirect(url_for('User.sign-in'))
        return redirect(next or url_for('wall'))


@login_required
def logout():
    logout_user()
    flash('You are sign out.')
    return redirect(url_for('User.sign-in'))


@login_required
def profile():
    return render_template('User/profile.html')


sign_up = SignUp.as_view('sign-up')
app_user.add_url_rule('/sign-up/', view_func=sign_up, methods=['GET', ])
app_user.add_url_rule('/sign-up/', view_func=sign_up, methods=['POST', ])

sign_in = SignIn.as_view('sign-in')
app_user.add_url_rule('/sign-in/', view_func=sign_in, methods=['GET', ])
app_user.add_url_rule('/sign-in/', view_func=sign_in, methods=['POST', ])

app_user.add_url_rule('/logout/', view_func=logout, methods=['GET', ])

app_user.add_url_rule('/profile/', view_func=profile, methods=['GET', ])
