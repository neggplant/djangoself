from .snippets import *


class HealthView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request):
        return Response("drf health")
