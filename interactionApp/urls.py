from django.urls import path

from .views import request_timeoff

urlpatterns = [
    path('request-timeoff', request_timeoff),
]
