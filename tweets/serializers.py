from rest_framework import serializers


class TweetSerializer(serializers.Serializer):

    pk = serializers.IntegerField(read_only=True)
    payload = serializers.CharField(max_length=180)
