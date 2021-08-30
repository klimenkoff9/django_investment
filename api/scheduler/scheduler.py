from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution

from datetime import date

import sys

# This is the function you want to schedule - add as many as you want and then register them in the start() function below
def run_orders():
    # get all users with daily buys (12pm)
    print(timezone.now(), file=sys.stdout);


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_orders, 'cron', second='*')
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)