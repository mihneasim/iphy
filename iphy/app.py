from flask import Flask
from path import path
import jinja2

from iphy import hip, db, auth, admin


DEFAULT_CONFIG = {
    'MONGODB_SETTINGS': {
        'DB': 'iphy',
    },
    'ASSETS_DEBUG': False,
    'CSRF_ENABLED': False,
}

BLUEPRINTS = (hip, auth)


def create_app(instance_path=None, config={}):
    app = Flask(__name__, instance_path=instance_path,
                      instance_relative_config=True)
    app.config.update(DEFAULT_CONFIG)
    app.config.from_pyfile('settings.py', silent=True)
    configure_db(app)
    configure_blueprints(app, BLUEPRINTS)
    configure_templates(app)
    configure_authentication(app)
    configure_admin(app)
    return app


def configure_db(app):
    db.initialize_db(app)


def configure_admin(app):
    admin.configure_admin(app)


def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        blueprint.initialize_app(app)


def configure_authentication(app):
    auth.login_manager.setup_app(app)


def configure_templates(app):
    instance_path = app.instance_path
    flask_loader = app.jinja_env.loader
    custom_path = str(path(instance_path)/'templates')
    app.jinja_env.loader = jinja2.ChoiceLoader([jinja2.FileSystemLoader(custom_path),
                                                flask_loader])
