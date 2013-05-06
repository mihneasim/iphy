from flask.ext.pymongo import PyMongo

_mongo = None


def mongo():
    return _mongo


def initialize_db(app):
    global _mongo
    _mongo = PyMongo(app)


# User: _id as username, pass, salt, email, first_name, last_name
# Post: title, author, description, content, files[{title, description, file, size}]

