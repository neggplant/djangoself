import random
import time

import requests

from application.celery import app as celery_app


@celery_app.task
def add(x, y):
    return x + y


@celery_app.task(acks_later=True)
def sleep(x, y):
    time.sleep(int(x))
    z = random.randint(1,1000)
    with open("tmp/{}-{}-{}--{}.txt".format(time.strftime("%Y%m%d-%H%M%S"), x, y, z), "w") as f:
        pass
    # url = "http://localhost:7777/health/sleep?sleep_time=4"
    # requests.get(url)
    return (x, y)
