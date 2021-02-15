from datetime import timedelta

from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from endpoint import constants as endpoint_constants
from endpoint import models as endpoint_models


class UrlSerializer(serializers.ModelSerializer):
    """
    Serializer for Url Model
    """
    time_left_before_expiry = serializers.SerializerMethodField()

    class Meta:
        model = endpoint_models.Url
        fields = ['url', 'time_left_before_expiry', 'no_of_hits']
        read_only_fields = ['no_of_hits', 'url']
    
    def get_time_left_before_expiry(self, instance):
        """
        Function to calculate time left before expiry of the url
        :param instance: Url model instance
        return: Time left in minutes
        """
        expiry_seconds = endpoint_constants.URL_EXPIRY_TIME_IN_SECONDS - (timezone.now() - instance.created_at).total_seconds()
        return int(expiry_seconds/60)
        


class EndPointDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for EndPointDetail Model
    """
    time_left_before_expiry = serializers.SerializerMethodField()
    time_after_hitting_url = serializers.SerializerMethodField()

    class Meta:
        model = endpoint_models.EndPointDetail
        fields = ['raw_body', 'headers', 'query_params', 'time_after_hitting_url', 'time_left_before_expiry']
        read_only_fields = ['headers', 'query_params', ]

    def get_time_left_before_expiry(self, instance):
        """
        Function to calculate time left before expiry of the url
        :param instance: Url model instance
        return: Time left in minutes
        """
        expiry_seconds = endpoint_constants.URL_EXPIRY_TIME_IN_SECONDS - (timezone.now() - instance.url.created_at).total_seconds()
        return int(expiry_seconds/60)

    def get_time_after_hitting_url(self, instance):
        """
        Function to calculate time left after hitting url
        :param instance: Url model instance
        return: Time passed in seconds
        """
        return int((timezone.now() - instance.created_at).total_seconds())

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
