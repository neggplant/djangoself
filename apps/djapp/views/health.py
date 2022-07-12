import logging

from django.http import HttpResponse

from django.views import View
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .. import models

logger = logging.getLogger(__name__)


class QustionChoiceView(View):

    def get(self, request):
        a = models.Question.objects.filter(id=1)
        from django.http import HttpResponse
        from django.utils.translation import gettext

        output = gettext("太阳:egg")
        return HttpResponse(output)
        # return HttpResponse("QustionChoiceView:{}".format(1))
