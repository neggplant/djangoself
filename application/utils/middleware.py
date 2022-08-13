import logging
import time

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class ResponseTimeViewMiddleware(MiddlewareMixin):
    """
    视图运行时长中间件
    """

    def process_request(self, request):
        self.start_time = time.time()

    def process_response(self, request, response):
        logger.debug("{}View time:{} s".format(request.path, round(time.time() - self.start_time, 3)))
        return response
