from datetime import timedelta

from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from endpoint import constants as endpoint_constants
from endpoint import models as endpoint_models


class UrlSerializer(serializers.ModelSerializer):
    time_left_before_expiry = serializers.SerializerMethodField()

    class Meta:
        model = endpoint_models.Url
        fields = ['url', 'time_left_before_expiry', 'no_of_hits']
        read_only_fields = ['no_of_hits', 'url']
    
    def get_time_left_before_expiry(self, instance):
        """
        """
        return (
            endpoint_constants.URL_EXPIRY_TIME_IN_SECONDS - (
                timezone.now() - instance.created_at
            ).total_seconds()
        )


class EndPointDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = endpoint_models.EndPointDetail
        fields = ['raw_body', 'headers', 'query_params']
        read_only_fields = ['headers', 'query_params']

    def create(self, validated_data):
        try:
            url = endpoint_models.Url.objects.get(url=self.context.get('url'))
        except:
            raise ValidationError(detail={'error': 'URL doesnot exist or is expired.'})
        else:
            validated_data['url'] = url
            obj = super().create(validated_data)
            obj.headers = self.context.get('headers')
            obj.query_params = self.context.get('query_params')
            obj.save()
            url.no_of_hits += 1
            url.save(update_fields=['no_of_hits'])
            return obj
