from .health import *
from .aggregate import *


class HealthView(View):

    def get(self, request):
        return HttpResponse("dj health")
