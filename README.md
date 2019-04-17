### Flask-Performance

A Flask extension to monitoring every **REAL** api request and collect it's performance in **REAL**-time.


#### Install by pip

> pip install flask-performance


#### Setup in Flask application

```python

from flask import Flask
from flask_performance import PerformanceCollector

app = Flask(__name__)

pc = PerformanceCollector(app)

# or by init_app() when you use factory pattern to creat flask app

pc = PerformanceCollector()
pc.init_app(app)

```


**And, That's all**