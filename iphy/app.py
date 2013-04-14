from flask import Flask
from iphy import hip

DEFAULT_CONFIG = {
    'MONGODB_SETTINGS': {
        'DB': 'iphy',
    },
    'ASSETS_DEBUG': False,
    'CSRF_ENABLED': False,
}

BLUEPRINTS = (hip,)

def create_app(instance_path=None, config={}):
    app = Flask(__name__, instance_path=instance_path,
                      instance_relative_config=True)
    app.config.update(DEFAULT_CONFIG)
    app.config.from_pyfile('settings.py', silent=True)
    configure_blueprints(app, BLUEPRINTS)
    return app

def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        blueprint.initialize_app(app)



