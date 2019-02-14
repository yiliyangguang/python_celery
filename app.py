from celery_app.task1 import add
from celery_app.task2 import multiply

if __name__ == '__main__':
    print('process start.....')
    result1 = add.delay(7, 7)
    print('add end')
    result2 = multiply.delay(3, 4)
    print('multiply end.....')
    print('process end....')
