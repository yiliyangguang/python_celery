BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
CELERY_TIMEZONE = 'Asia/Shanghai'

# task model
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)
