import time
from datetime import datetime

import requests
from flask import request


class PerformanceCollector(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if app is None:
            raise Exception('init_app should have app parameter')

        if app.config['METRIC_DSN'] is None or len(app.config['METRIC_DSN']) == 0:
            raise Exception('METRIC_DSN was not found in config')

        app.api_performance_collector = self
        app.before_request(self._before_request)
        app.after_request(self._after_request)
        self.app = app

    def _before_request(self):
        self.app.g.start_time = time.time()
        

    def _after_request(self, response):
        time_used = time.time() - self.app.g.start_time
        doc = {
            "time_used": time_used,
            "created_at": str(datetime.utcnow()),
            "path": request.path,
            "status_code": response.status_code,
            "method": request.method,
            "endpoint": request.endpoint
        }
        try:
            requests.post(
                url='{}'.format(self.app.config['METRIC_DSN']),
                json=doc,
                timeout=0.5
            )
        except:
            pass

        return response
