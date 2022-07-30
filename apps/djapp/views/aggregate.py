from django.db.models import Count
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView

from .. import models


class AggregateView(APIView):
    """
    https://docs.djangoproject.com/zh-hans/4.0/topics/db/aggregation/

    需要注意 annotate() 和 filter() 子句的顺序，以及annotate() 和 values() 的顺序
    比如：
        出版者A有两本评分4和5的书。
        出版者B有两本评分1和4的书。
        出版者C有一本评分1的书。

    a, b = Publisher.objects.annotate(num_books=Count('book', distinct=True)).filter(book__rating__gt=3.0)
    a, a.num_books
    (<Publisher: A>, 2)
    b, b.num_books
    (<Publisher: B>, 2)

    a, b = Publisher.objects.filter(book__rating__gt=3.0).annotate(num_books=Count('book'))
    a, a.num_books
    (<Publisher: A>, 2)
    b, b.num_books
    (<Publisher: B>, 1)
    """

    def get(self, request):
        #
        q = models.Book.objects.annotate(Count('authors'), Count('store'))
        # todo：聚合查询时候distinct=True参数确认
        print(q)
        return Response(q)


class RedirectView(APIView):

    def get(self, request):
        # 重定向接口
        return HttpResponseRedirect("/drf/snippets/aggregate/")
