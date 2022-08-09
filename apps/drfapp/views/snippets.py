from django.db.models import Count, Avg
from django.views.decorators.cache import cache_page

from ..models import Snippet
from ..serializers import SnippetSerializer, SnippetSerializer1
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


class SnippetAggregate(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        # 分组查询values，
        # values中的唯一的数量
        # 注意若模型meta中包含order，则后面必须加order_by，否则出错，也会包含在分组里，
        code_number = snippets.values('code').annotate(code_count=Count('id')).filter(code__gt=0).order_by('code')
        print(code_number)
        avg_line = snippets.aggregate(Avg("linenos"))
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    @cache_page(60 * 15)
    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Snippet.objects.filter(pk=pk).defer("title")
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        print(snippet[0].code)
        serializer = SnippetSerializer1(snippet, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Snippets(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

