import uuid
from datetime import timedelta

from django.db import models
from django.utils import timezone

from endpoint import constants


class TimeModel(models.Model):
    """
    """
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Url(TimeModel, models.Model):
    """
    """
    url = models.CharField(max_length=100, unique=True)
    is_expired = models.BooleanField(default=False)
    no_of_hits = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.url = self.generate_url()
        return super(Url, self).save(*args, **kwargs)

    def generate_url(self):
        return uuid.uuid4()

    def check_expiry(self):
        return timezone.now() - self.created_at > timedelta(days=constants.URL_EXPIRY_TIME_IN_SECONDS)

    def __str__(self):
        return self.url


class EndPointDetail(TimeModel, models.Model):
    """
    """
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    headers = models.TextField()
    raw_body = models.TextField()
    query_params = models.TextField()
