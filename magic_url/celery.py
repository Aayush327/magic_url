from __future__ import absolute_import
import os

from celery import Celery

from endpoint import constants as endpoint_constants


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magic_url.settings')
app = Celery('magic_url')

app.config_from_object('django.conf:settings')

app.conf.beat_schedule = {
    'delete-expired-urls': {
        'task': 'endpoint.tasks.delete_expired_urls',
        'schedule': endpoint_constants.PERIODIC_TASKS_SCHEDULE_TIME
    }
}

app.autodiscover_tasks()
