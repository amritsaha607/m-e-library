from django.urls import path

from .views import (approve_timeoff_request, decline_timeoff_request,
                    request_timeoff)

urlpatterns = [
    path('request-timeoff', request_timeoff),
    path('approve-timeoff', approve_timeoff_request),
    path('decline-timeoff', decline_timeoff_request),
]
