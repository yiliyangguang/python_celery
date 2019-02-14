import time

from celery_app import app


@app.task
def multiply(x, y):
    print('multiply calculate start....')
    time.sleep(3)
    return x * y
