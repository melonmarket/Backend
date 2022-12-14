from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        if self.get_next_link() is None:
            return Response(OrderedDict([("results", data), ("final", 1)]))
        return Response(OrderedDict([("results", data), ("final", 0)]))
