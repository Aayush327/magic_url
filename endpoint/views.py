from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, status
from rest_framework.response import Response

from endpoint import models as endpoint_models
from .serializers import UrlSerializer


class CreateUrlView(generics.ListCreateAPIView):
    
    queryset = endpoint_models.Url.objects.all().order_by('-created_at')
    serializer_class = UrlSerializer
