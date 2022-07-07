import logging
import time

from django.core.cache import cache
from django.http import JsonResponse

# Create your views here.
from django.views import View

from apps.baseapp import models
from apps.baseapp.tasks import add, sleep

logger = logging.getLogger(__name__)


def async_sleep(request):
    x = request.GET.get("x")
    y = request.GET.get("y")
    sleep.delay(x, y)
    return JsonResponse("async_sleep:{},{}".format(x, y), safe=False)


def sleep_view(request):
    sleep_time = int(request.GET.get("sleep_time", 1))
    time.sleep(sleep_time)
    return JsonResponse("sleep_view:{}".format(sleep_time), safe=False)


class AsyncSleep(View):

    def get(self, request):
        x = request.GET.get("x")
        y = request.GET.get("y")
        cache.get('my_key')
        sleep.delay(x, y)
        return JsonResponse("async_sleep:{},{}".format(x, y), safe=False)
