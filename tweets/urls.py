from django.urls import path
from . import views

urlpatterns = [
    path("", views.see_all_tweets),
    path("<int:tweet_pk>", views.see_one_tweet),
]