from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TweetSerializer
from .models import Tweet


@api_view(["GET"])
def all_tweets(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)
