from rest_framework import serializers
from nginx_log_parser_app.models import Nginx_log

class Nginx_log_serializer(serializers.ModelSerializer):
    class Meta:
        model = Nginx_log
        fields = '__all__'
