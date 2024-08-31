from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from nginx_log_parser_app.models import Nginx_log
from nginx_log_parser_app.seralizers import Nginx_log_serializer


class Nginx_log_ViewSet(viewsets.ModelViewSet):
    queryset = Nginx_log.objects.all()
    serializer_class = Nginx_log_serializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['ip_address', 'uri', 'time']
    search_fields = ['ip_address', 'uri', 'time', 'http_method']
    ordering_fields = ['time', 'id', 'response_size']
    ordering = ['id']

