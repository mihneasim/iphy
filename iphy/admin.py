from flask.ext import wtf
from flask.ext.admin.contrib.pymongo import ModelView
from flask.ext import admin

from iphy.db import mongo


class PostForm(wtf.Form):
    title = wtf.TextField('Title')
    description = wtf.TextAreaField('Description')
    content = wtf.TextAreaField('Body')


class PostView(ModelView):
    column_list = ('title', 'description', 'content')
    form = PostForm


def configure_admin(app):
    with app.app_context():
        administration = admin.Admin(app)
        administration.add_view(PostView(mongo().db.post))
