from django.db import models
from django.db.models import Model


class Nginx_log(Model):
    ip_address = models.GenericIPAddressField()
    time = models.DateTimeField()
    http_method = models.CharField(max_length=10)
    uri = models.CharField(max_length=255)
    response_code = models.IntegerField()
    response_size = models.BigIntegerField()

    def __str__(self):
        return f"{self.time} | {self.ip_address} | {self.http_method} {self.uri} | {self.response_code} | {self.response_size}"
