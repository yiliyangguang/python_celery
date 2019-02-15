import time

from celery.task import Task


class CourseTask(Task):
    name = 'course.task'

    def run(self, *args, **kwargs):
        print('start course tasks')
        time.sleep(5)
        print('args = {}, kwargs = {}'.format(args, kwargs))
        print('end course tasks...')
