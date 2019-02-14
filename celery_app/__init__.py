from celery import Celery

app = Celery('myCelery')
app.config_from_object('celery_app.celery_config')
