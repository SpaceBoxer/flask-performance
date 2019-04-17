### Flask-Performance

A Flask extension to monitoring every **REAL** api request and collect it's performance in **REAL**-time.


#### 1、Install by pip

> pip install flask-performance

#### 2、Generate DSN

Go to https://status.spacebox.fun, sign up  or login. Create a new project or new team (if you are working in a company, we highly recommend you create Team first and put every project into the Team afterward)

And after suceccfully create a project, you are given a DSN url, which is the API your project performance data will send to.

e.g.

> https://metrics.spacebox.fun/v1/collector/c5b35bc078844a59a15dd506e08f3ae6


#### 3、Setup & configuration in your Flask project

```python

from flask import Flask
from flask_performance import PerformanceCollector

app = Flask(__name__)

pc = PerformanceCollector(app)
app.config['METRIC_DSN'] = 'https://metrics.spacebox.fun/v1/collector/c5b35bc078844a59a15dd506e08f3ae6'

# or by init_app() when you use factory pattern to creat flask app
app = create_app()

pc = PerformanceCollector()
pc.init_app(app)
app.config['METRIC_DSN'] = 'https://metrics.spacebox.fun/v1/collector/c5b35bc078844a59a15dd506e08f3ae6'

```

You can also put **METRIC_DSN** into your project `config.py` file and use Flask's `from_pyfile`.


in your `config.py` file

> METRIC_DSN = 'https://metrics.spacebox.fun/v1/collector/c5b35bc078844a59a15dd506e08f3ae6'

in your project `app.py` file

> app.from_pyfile('config')


**And, That's all**, just go to your https://status.spacebox.fun platform to check your project all API performance in real-time.