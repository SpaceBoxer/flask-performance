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
app.config['METRIC_DSN'] = 'https://metrics.spacebox.fun/v1/collector/c5b35bc078844a59a15dd506e08f3ae6'

pc = PerformanceCollector(app)

# or by init_app() when you use factory pattern to creat flask app
app = create_app()
app.config['METRIC_DSN'] = 'https://metrics.spacebox.fun/v1/collector/c5b35bc078844a59a15dd506e08f3ae6'

pc = PerformanceCollector()
pc.init_app(app)

```

You can also put **METRIC_DSN** into your project `config.py` file and use Flask's `from_pyfile`.


in your `config.py` file

> METRIC_DSN = 'https://metrics.spacebox.fun/v1/collector/c5b35bc078844a59a15dd506e08f3ae6'

in your project `app.py` file

> app.from_pyfile('config')


**And, That's ALL**, just go to your https://status.spacebox.fun platform to check your project all API performance in real-time.


#### 4、Performance problem

Chance is that you will ask: Will this performance collector affect your project's performance ?

the short answer is: yes.

**BUT**, the affects is limit maximus to `500ms`. We set the timeout to `500ms` when send the performance data to the API.

And we implemented this API in a asynchronous way, which means when we receive your project performance data every time we will response immediately and throw the save performance data task to a task queue (which is Celery). In most case, the API will reponse under 100ms.