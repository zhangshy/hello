from flask import Flask, flash, redirect, render_template, \
    request, url_for
from flask.ext.wtf import Form
from wtforms.fields import StringField, BooleanField
from wtforms.validators import DataRequired
from flask.ext.sqlalchemy import SQLAlchemy

from blog import app

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/idlogin', methods=['GET', 'POST'])
def idlogin():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('idlogin.html',
                    title = 'Sign In',
                    form = form,
                    providers = app.config['OPENID_PROVIDERS'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

