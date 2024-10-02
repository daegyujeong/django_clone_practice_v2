from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet


# Create your views here.
def see_all_tweets(request):
    tweets = Tweet.objects.all()
    return render(
        request,
        "all_tweets.html",
        {
            "tweets": tweets,
            "title": "Hello! I am Tweet, My new name is X!",
        },
    )


def see_one_tweet(request, tweet_pk):
    try:
        tweet = Tweet.objects.get(pk=tweet_pk)
        return render(
            request,
            "tweet_detail.html",
            {
                "tweet": tweet,
            },
        )
    except Tweet.DoesNotExist:
        return render(
            request,
            "tweet_detail.html",
            {
                "not_found": True,
            },
        )