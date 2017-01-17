
from flask.views import View


class WarmupView(View):

    def dispatch_request(self):
        return "I'am ready"


