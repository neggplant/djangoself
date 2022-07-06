import logging
import time

from django.core.cache import cache
from django.http import JsonResponse

# Create your views here.
from django.views import View

from apps.baseapp import models
from apps.baseapp.tasks import add, sleep

logger = logging.getLogger(__name__)


class QustionChoiceView(View):

    def get(self, request):
        sleep_time = int(request.GET.get("sleep_time", 1))
        time.sleep(sleep_time)
        return JsonResponse("sleep_view:{}".format(sleep_time), safe=False)
