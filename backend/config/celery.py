from __future__ import absolute_import
import os
from kombu import Queue
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.conf.task_queues = (
    Queue('fast'),
    Queue('slow'),
)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
