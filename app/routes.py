from app import app
from flask import Flask, render_template, redirect, flash
from flask import request


from base import session

from app.models import User



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/search')
    return render_template('login.html', title='Log In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(form.username.data,form.email.data, form.password.data)
        session.add(new_user)
        session.commit()
        flash('Thanks for registrering, You are a registered user now !!')
        return redirect('/login')
    return render_template('register.html', titles = 'Register', form = form)



@app.route('/search', methods =['GET', 'POST'])
def search():
    return render_template('search.html', title='Search')
