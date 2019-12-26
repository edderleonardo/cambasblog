from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'cambasBlog.settings')

app = Celery('cambasBlog')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=0, minute=0, day_of_week=1),
        do_nothing.s(),
        name='Do nothing every week')
    sender.add_periodic_task(
        10.0, test.s('hello universe'), name='add every 10')


@app.task
def do_nothing():
    pass


@app.task
def test(arg):
    print(arg)
