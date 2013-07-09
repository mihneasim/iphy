import flask

from iphy.db import mongo


hip = flask.Blueprint('hip', __name__)


def initialize_app(app):
    app.register_blueprint(hip)


@hip.route("/")
def home():
    posts = mongo().db.post.find({'visible': True}).sort("date", -1).limit(20)
    return flask.render_template("home.html", posts=posts)

@hip.route("/h/<slug>/")
def post(slug):
    post = mongo().db.post.find_one({"slug": slug})
    return flask.render_template("post.html", post=post)
