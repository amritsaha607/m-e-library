from django.urls import path

from . import views

urlpatterns = [
    path('friend-req', views.request_friendship, name='friend_request'),
    path('follow', views.follow_user, name='follow'),
]
