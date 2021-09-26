from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution

from ..utils import place_order
from datetime import date

from ..models import Orders

import sys

# example for weekly orders, change the date on line 23 to the date you want to run the orders, or if you have multiple orders write if statemets


def run_orders():
    """run the job if today's day is a week from created_at"""
    print("Running orders...", file=sys.stdout)
    # get all jobs
    orders = Orders.objects.all()
    # get today's date
    today = date.today()
    # iterate through jobs
    for order in orders:
        # get the date of the job
        order_date = order.created_at.date()
        # if the job is a week from today
        if today == order_date + timezone.timedelta(days=7):
            # run the job
            place_order(order.funds, order.currency, order.coinbase_account)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_orders, 'cron', hour='12')
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)
