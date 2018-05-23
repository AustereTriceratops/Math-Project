from flask import Blueprint, request, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, DataRequired

bp = Blueprint('auth', __name__, url_prefix='/auth')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    login_form = LoginForm()
    if request.method == 'POST':
        k = 1

    return render_template('auth/login.html', form=login_form)


@bp.route('/logout')
def logout():
    return redirect(url_for('index'))


@bp.route('/register', methods=('GET', 'POST'))
def register():
    register_form = RegisterForm()
    if request.method == 'POST':
        k = 1

    return render_template('auth/register.html', form=register_form)
