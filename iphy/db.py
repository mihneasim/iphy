from flask.ext.pymongo import PyMongo
from pymongo import ASCENDING, DESCENDING

_mongo = None


def mongo():
    return _mongo


def initialize_db(app):
    global _mongo
    _mongo = PyMongo(app)
    with app.app_context():
        _mongo.db.post.create_index([("date", DESCENDING)])


# User: _id as username, pass, salt, email, first_name, last_name
# Post: title, author, description, content, files[{title, description, file, size}]

