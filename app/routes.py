from app import app,db
from flask import Flask, render_template, redirect, flash
from flask import request

from forms import LoginForm, RegisterForm
from base import session
from app.models import User

#####login#####
from flask_login import current_user, login_user, login_required
from app.models import User


@app.route('/')
@app.route('/home')
@login_required
def home():
    return render_template('home.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect('/home')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)

        return redirect('/search')
    return render_template('login.html', title='Log In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(form.username.data,form.email.data)
        new_user.set_password(form.password.data)
        session.add(new_user)
        session.commit()
        flash('Thanks for registrering, You are a registered user now !!')
        return redirect('/login')
    return render_template('register.html', titles = 'Register', form = form)



@app.route('/search', methods =['GET', 'POST'])
def search():
    return render_template('search.html', title='Search')
