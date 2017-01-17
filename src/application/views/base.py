from flask import render_template
from flask.views import View


class BaseView(View):

    def dispatch_request(self):
        return render_template('hello.html')
