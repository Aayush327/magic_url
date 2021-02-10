from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^create/',views.CreateUrlView.as_view(), name='create_url'),
]
