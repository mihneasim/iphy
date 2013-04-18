import datetime

from flask import (Blueprint, request, render_template, redirect, url_for,
                   flash, g)
from flask.ext.login import LoginManager
from flask.ext import wtf
from flask.ext import login as flask_login


from iphy.forms import LoginForm
from iphy.models import User
from iphy import plugauth


auth = Blueprint('auth', __name__)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def load_user_in_g():
    g.user = flask_login.current_user


def initialize_app(app):
    app.register_blueprint(auth)
    app.before_request(load_user_in_g)

def get_user(userid):
    """ Get user document object """
    return None # TODO, wip

login_manager.user_loader(get_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username, password = request.form['username'], request.form['password']
        if plugauth.login_user(username, password):
            user = get_user(username)
            flask_login.login_user(user)
            flash('Logged in successfully as %s %s (%s).' %
                  (user.first_name, user.last_name, user.id))
            user.last_login = datetime.datetime.utcnow()
            user.save(safe=False)
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