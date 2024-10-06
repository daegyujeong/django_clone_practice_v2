from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TweetSerializer
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .models import Tweet


class Tweets(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
