import logging
import time

from django.core.cache import cache
from django.http import JsonResponse

# Create your views here.
from django.views import View
from kombu import Connection

from application.settings import BROKER_URL
from apps.baseapp import models
from apps.baseapp.tasks import add, sleep

logger = logging.getLogger(__name__)


def async_sleep(request):
    x = request.GET.get("x")
    y = request.GET.get("y")
    sleep.delay(x, y)
    return JsonResponse("async_sleep:{},{}".format(x, y), safe=False)


class AsyncSleep(View):

    def get(self, request):
        x = request.GET.get("x")
        y = request.GET.get("y")
        cache.get('my_key')
        sleep.delay(x, y)
        return JsonResponse("async_sleep:{},{}".format(x, y), safe=False)


class RabbitMQView(View):

    def get(self, request):
        # 设置rabbitmq超时时长
        with Connection(BROKER_URL, connection_timeout=1) as conn:
            producer = conn.Producer(serializer='json')
            producer.publish("111",
                             exchange="celery", routing_key="celery",
                             declare=["celery"])
        return JsonResponse("RabbitMQView send", safe=False)
