import logging

from django.core.cache import cache
from django.http import JsonResponse, HttpResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .. import models

logger = logging.getLogger(__name__)


class QustionChoiceView(View):
    @swagger_auto_schema(
        operation_description="apiview post description override",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['page', 'pageSize'],
            properties={
                'page': openapi.Schema(type=openapi.TYPE_NUMBER),
                'pageSize': openapi.Schema(type=openapi.TYPE_NUMBER),
            },
        ),
        security=[], tags=['WlUser'], operation_summary='列表')
    def get(self, request):
        a = models.Question.objects.filter(id=1)
        print(a[0].question_text)
        return HttpResponse("QustionChoiceView:{}".format(1))
