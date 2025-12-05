from django.urls import path

from .views import (AssociateLookupView, approve_timeoff_request,
                    decline_timeoff_request, request_timeoff, store_check_in,
                    store_check_out)

urlpatterns = [
    path('request-timeoff', request_timeoff),
    path('approve-timeoff', approve_timeoff_request),
    path('decline-timeoff', decline_timeoff_request),

    path('store-check-in', store_check_in),
    path('store-check-out', store_check_out),

    path('associate', AssociateLookupView.as_view()),
]
