import flask


hip = flask.Blueprint('hip', __name__)


def initialize_app(app):
    app.register_blueprint(hip)


@hip.route("/")
def hello():
    return flask.render_template("home.html")

