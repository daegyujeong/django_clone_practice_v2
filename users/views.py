from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from .models import User
from tweets.models import Tweet
from tweets.serializers import TweetSerializer


@api_view(["GET"])
def tweets_by_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise NotFound
    tweets = Tweet.objects.filter(user=user)
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)
