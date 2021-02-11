from django.contrib import admin

from .models import EndPointDetail, Url

admin.site.register(Url)
admin.site.register(EndPointDetail)
