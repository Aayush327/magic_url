from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from endpoint import (
    models as endpoint_models,
    serializers as endpoint_serializers,
    utils as endpoint_utils
)


class UrlViewSet(ModelViewSet):
    """
    """
    queryset = endpoint_models.Url.objects.all().order_by('-created_at')
    serializer_class = endpoint_serializers.UrlSerializer

    def list(self, request, *args, **kwargs):
        endpoint_utils.update_expiry_of_urls()
        queryset = self.queryset.filter(is_expired=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "url_list":serializer.data
        })
        

class EndPointDetailView(generics.CreateAPIView, generics.ListAPIView):
    """
    """
    queryset = endpoint_models.EndPointDetail.objects.all().order_by('-created_at')
    serializer_class = endpoint_serializers.EndPointDetailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data={
                'raw_body': request.data['raw_body'],
            },
            context={
                'url': kwargs.get('url'),
                'headers': request.headers,
                'query_params': dict(request.GET)
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(url__url=kwargs.get('url'))[:4]
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "endpoint_detail_list": serializer.data
        })

