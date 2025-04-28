from django.db import models
from django.contrib.postgres.fields import JSONField

class FormData(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    additional_inputs = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)