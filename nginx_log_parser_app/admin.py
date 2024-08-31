from django.contrib import admin
from nginx_log_parser_app.models import Nginx_log


@admin.register(Nginx_log)
class Nginx_log_admin(admin.ModelAdmin):
    list_display = ('time', 'ip_address', 'http_method', 'uri', 'response_code', 'response_size')
    list_filter = ('http_method', 'response_code', 'uri')
    search_fields = ('ip_address', 'uri')
