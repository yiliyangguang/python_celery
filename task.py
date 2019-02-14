import time
from celery import Celery

broker = 'redis://localhost:6379/1'
backend = 'redis://localhost:6379/2'
app = Celery('mytask', broker=broker, backend=backend)


@app.task
def add(x, y):
    print('enter task....')
    time.sleep(10)
    return x + y
