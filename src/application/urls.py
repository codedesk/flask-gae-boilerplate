"""
urls.py

URL dispatch route mappings and error handlers

"""
from flask import render_template
from application import app
from application.views.warmup import WarmupView
from application.views.base import BaseView

# See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
app.add_url_rule('/_ah/warmup',
                 'public_warmup',
                 view_func=WarmupView.as_view('public_warmup'))
app.add_url_rule('/',
                 'public_index',
                 view_func=BaseView.as_view('public_index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
