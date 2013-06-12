import datetime
import hashlib
import string
import random

from flask import (Blueprint, request, render_template, redirect, url_for,
                   flash, g)
from flask.ext.login import LoginManager, UserMixin
from flask.ext import login as flask_login

from iphy.db import mongo
from iphy.forms.auth import LoginForm


auth = Blueprint('auth', __name__)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


class User(UserMixin, dict):
    """ implement required user interface for Flask-Login """

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.id = self['_id']


def create_user(username, password, email, first, last):
    doc = {'_id': username, 'email': email, 'first_name': first,
           'last_name': last}
    doc['salt'] = ''.join([random.choice(string.printable) for x in range(10)])
    doc['pass'] = get_crypt(password, doc['salt'])
    return mongo().db.user.insert(doc)


def load_user_in_g():
    g.user = flask_login.current_user


def initialize_app(app):
    app.register_blueprint(auth)
    app.before_request(load_user_in_g)


def get_user(userid):
    """ Get user document object """
    user = mongo().db.user.find_one({"_id": userid})
    if user:
        return User(user)


def get_crypt(password, salt):
    crypt = "%s-%s" % (salt, password)
    for i in range(101):
        crypt = "%s-%s-%s" % (crypt, salt, crypt)
        crypt = hashlib.sha1(crypt).hexdigest()
    return crypt


def login_user(username, password):
    user = get_user(username)
    if not user:
        return None
    return get_crypt(password, user['salt']) == user['pass'] and user


login_manager.user_loader(get_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username, password = request.form['username'], request.form['password']
        user = login_user(username, password)
        if user:
            flask_login.login_user(user)
            flash('Logged in successfully as %s %s (%s).' %
                  (user['first_name'], user['last_name'], user['_id']))
            user['last_login'] = datetime.datetime.utcnow()
            mongo().db.user.save(user)
            resp = redirect(request.args.get("next") or url_for('hip.home'))
            return resp
        else:
            flash('Bad username or password.')

    return render_template('login.html', form=form)


@auth.route("/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    flash("You have successfully logged out.")
    resp = redirect(url_for('hip.home'))
    return resp