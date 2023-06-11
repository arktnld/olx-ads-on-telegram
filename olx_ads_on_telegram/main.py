#!/usr/bin/env /home/arktnld/.cache/pypoetry/virtualenvs/olx-scrapy-IeO-6KNa-py3.11/bin/python
import os

from apscheduler.schedulers.blocking import BlockingScheduler
from olx_ads_on_telegram.search import run_search
import asyncio

def start():
    print('Start search')
    run_search()
    print("End, wait 60 minutes")

print('Create scheduler')
scheduler = BlockingScheduler()
print('Add job')
scheduler.add_job(start, 'interval', minutes=60)
print('Start scheduler')
scheduler.start()
