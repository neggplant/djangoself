import logging

from django.http import HttpResponse

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
        return HttpResponse("QustionChoiceView:{}".format(1))
