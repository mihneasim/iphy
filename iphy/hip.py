from flask import Blueprint


hip = Blueprint('hip', __name__)


def initialize_app(app):
    app.register_blueprint(hip)


@hip.route("/")
def hello():
    return "Iphy!"

