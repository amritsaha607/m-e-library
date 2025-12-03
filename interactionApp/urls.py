from django.urls import path

from . import views

urlpatterns = [
    path('rent-article', views.rent_article, name='rent-article'),
]
