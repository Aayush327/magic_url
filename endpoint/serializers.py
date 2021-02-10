from .models import Url, EndPointDetail
from rest_framework import serializers


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['url']


class EndPointDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndPointDetail
        fields = ['url', 'headers', 'raw_body', 'query_params']
