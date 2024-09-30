"""
URL configuration for fixmybrick_backend project.

"""
from django.contrib import admin
from django.urls import path, include

from .api import api

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('service/', include('service.urls')),
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
