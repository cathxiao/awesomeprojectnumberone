from abc import ABCMeta, ABC, abstractmethod, abstractproperty
from flask import Flask, request, url_for, redirect, render_template, flash
from flask_login import LoginManager, login_user
from flask_wtf import Form, FlaskForm
from wtforms import StringField, BooleanField, PasswordField, validators
from wtforms.validators import InputRequired, Email, Length
from urllib.parse import urlparse, urljoin
from flask_bootstrap import Bootstrap

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '2'
Bootstrap(app)
login_manager = LoginManager()


class LoginForm(Form):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(Form):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


class User(ABC):
    authenticated = False
    active = False
    anonymous = False
    id = None

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return self.anonymous

    def get_id(self):
        return self.id


@login_manager.user_loader
def load_user(user_id):
    pass  # TODO: unimplemented for the moment


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


@app.route('/')
def index():
    return render_template('Home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/Profile')
def prof():
    return render_template('Profile.html')


@app.route('/carousel')
def caro():
    return render_template('carousel.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cond = username.isupper() or username.islower()
        if cond is True:
            return render_template('Profile.html', username=username, password=password)
    flash('Invalid password provided', 'error')
    return render_template('login.html')


if __name__ == "__main__":
    app.run()