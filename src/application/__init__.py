from flask import Flask
import os

__author__ = "vasanth"

app = Flask(__name__)

app.config.from_object('application.settings.Development')
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

import urls