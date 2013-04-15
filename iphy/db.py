from flask.ext.pymongo import PyMongo

mongo = None


def initialize_db(app):
    global mongo
    mongo = PyMongo(app)


# User: _id as username, pass, salt, email, first_name, last_name
# Post: title, author, description, content, files[]

