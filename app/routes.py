from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
def homep():
    return render_template('home.html')
@app.route('/index')
def index():
    return render_template('layout.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/login',methods=['GET','POST'])
def log():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/home')
    return render_template('login.html',form=form)
@app.route('/register')
def reg():
    return render_template('reg.html')
