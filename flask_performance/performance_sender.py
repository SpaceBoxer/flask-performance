import time
from datetime import datetime
import requests


class PerformanceSender(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        '''

        '''
        app.api_performance_sender = self
        app.before_request(self._before_request)
        app.after_request(self._after_request)
        self.app = app

    def _before_request(self):
        self.app.g.start_time = time.time()
        


    def _after_request(self, response):
        time_used = time.time() - self.app.g.start_time
        doc = {
            "time_used": time_used,
            "created_at": str(datetime.utcnow())
        }
        try:
            requests.post(url='https://www.baidu.com', json=doc, timeout=1)
        except:
            pass

        return response
