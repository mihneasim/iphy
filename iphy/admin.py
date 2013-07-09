import os
from datetime import datetime

from flask.ext import wtf
from flask.ext.admin.contrib.pymongo import ModelView
from flask.ext.admin import BaseView
from flask.ext import admin as flask_admin
from flask.ext import login
from flask.ext.uploads import (UploadSet, AllExcept, SCRIPTS, EXECUTABLES)

from iphy.db import mongo


files = UploadSet('files', AllExcept(SCRIPTS + EXECUTABLES))


class AuthView(BaseView):
    def is_accessible(self):
        return login.current_user.is_authenticated()


class PostForm(wtf.Form):
    title = wtf.TextField('Title')
    description = wtf.TextAreaField('Description')
    content = wtf.TextAreaField('Body')
    filefield = wtf.FileField('Files')
    visible = wtf.BooleanField('Published', default=True)


class PostView(ModelView, AuthView):
    column_list = ('title', 'description', 'content', 'visible')
    form = PostForm

    def on_model_change(self, form, model):
        super(PostView, self).on_model_change(form, model)
        # generate slug
        # TODO for model['slug']
        # file upload
        ffile = model['filefield']
        if ffile.filename:
            filename = files.save(model['filefield'])
            model.setdefault('files', []).append({'file': filename})
        del model['filefield']
        # set author if missing
        if not model.get('author'):
            model['author'] = login.current_user['_id']
        if not model.get('date'):
            model['date'] = datetime.now()

    def on_model_delete(self, model):
        for ffile in model['files']:
            abspath = files.path(ffile['file'])
            os.unlink(abspath)

def configure_admin(app):
    with app.app_context():
        administration = flask_admin.Admin(app)
        administration.add_view(PostView(mongo().db.post))
