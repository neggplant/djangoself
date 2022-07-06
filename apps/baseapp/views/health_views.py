import logging

from django.http import JsonResponse

# Create your views here.
from apps.baseapp import models
from apps.baseapp.tasks import add, sleep

logger = logging.getLogger(__name__)


def health(request):
    return JsonResponse("baseapp health", safe=False)
