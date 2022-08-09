import logging
import time

from django.http import JsonResponse

# Create your views here.
from application.utils.signals import some_signal

logger = logging.getLogger(__name__)


def health(request):
    return JsonResponse("baseapp health", safe=False)


def sleep_view(request):
    sleep_time = int(request.GET.get("sleep_time", 1))
    time.sleep(sleep_time)
    return JsonResponse("sleep_view:{}".format(sleep_time), safe=False)


def exc_view(request):
    raise ImportError
    # return JsonResponse("baseapp health", safe=False)


def signal_view(request):
    some_signal.send(signal_view)
    return JsonResponse("signal_view", safe=False)
