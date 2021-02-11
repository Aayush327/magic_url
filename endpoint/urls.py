from django.urls import include, path
from rest_framework import routers

from endpoint import views as endpoint_views

router = routers.SimpleRouter()
router.register('url', endpoint_views.UrlViewSet)

urlpatterns = [
    path('test/<slug:url>/',endpoint_views.EndPointDetailView.as_view(), name='post-data'),
]

urlpatterns += router.urls
