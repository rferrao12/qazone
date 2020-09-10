from flask import render_template
from app import app



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
@app.route('/login')
def log():
    return render_template('login.html')
@app.route('/register')
def reg():
    return render_template('reg.html')
