import logging

from django.core.mail import send_mail
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


class SendEmailView(View):

    def get(self, request):

        send_mail(
            'Subject here',
            'Here is the message.',
            'cq4050@163.com',
            ['cq4050@163.com'],
            fail_silently=False,
        )
        return HttpResponse("send_mail success")