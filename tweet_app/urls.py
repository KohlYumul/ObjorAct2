from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_tweet_view, name='create_tweet'),
]