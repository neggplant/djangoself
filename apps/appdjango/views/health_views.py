import logging

from django.core.cache import cache
from django.http import JsonResponse, HttpResponse

# Create your views here.
from django.views import View

from .. import models

logger = logging.getLogger(__name__)


class QustionChoiceView(View):

    def get(self, request):
        a = models.Question.objects.filter(id=1)
        print(a[0].question_text)
        return HttpResponse("QustionChoiceView:{}".format(1))
