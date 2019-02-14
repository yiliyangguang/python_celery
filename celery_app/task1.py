import time

from celery_app import app


@app.task
def add(x, y):
    print('add calculate start.....')
    time.sleep(3)
    return x + y
