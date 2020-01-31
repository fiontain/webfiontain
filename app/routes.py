from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'SaberFan69'}
    return render_template('index.html', title='Home', user=user)


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
