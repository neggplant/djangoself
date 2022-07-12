from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView

from .. import models


class AggregateView(APIView):

    def get(self, request):
        #
        q = models.Book.objects.annotate(Count('authors'), Count('store'))
        print(q)
        return Response(q)