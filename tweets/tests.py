from rest_framework.test import APITestCase
from rest_framework import status
from .models import Tweet
from users.models import User


class Tweets_Test(APITestCase):
    PAYLOAD = 'this is test tweet'
    PAYLOAD_2 = 'this is test tweet2'
    URL = "/api/v1/tweets/"

    def setUp(self):
        user = User.objects.create_user(username='testuser')
        user.set_password("123")
        user.save()
        self.user = user
        self.client.login(username="testuser", password="123")
        Tweet.objects.create(user=self.user, payload=self.PAYLOAD)
        Tweet.objects.create(user=self.user, payload=self.PAYLOAD_2)
        print("my ID:", self.user.id)

    def test_get_tweets(self):
        response = self.client.get(self.URL)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 2)
        self.assertEqual(
            data[0]["payload"],
            self.PAYLOAD,
        )
        self.assertEqual(
            data[0]["user"],
            self.user.id,
        )

    def test_post_tweets(self):

        payload = 'this is test tweet2'
        response = self.client.post(self.URL, {
            'payload': payload,
            "user": self.user.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.json()
        print("test_post_tweets :", data)
        self.assertEqual(data["payload"], payload)


class Tweet_Detail_Test(APITestCase):
    URL_Valid = "/api/v1/tweets/1"
    URL_Invalid = "/api/v1/tweets/2"
    payload = "test tweet"
    payload_update = "update tweet"

    def setUp(self):
        user = User.objects.create_user(username='testuser')
        user.set_password("123")
        user.save()
        self.user = user
        self.client.login(username="testuser", password="123")
        Tweet.objects.create(payload=self.payload, user=self.user)

    def test_tweet_not_found(self):
        response = self.client.get(self.URL_Invalid)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_tweet(self):
        response = self.client.get(self.URL_Valid)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        print("test_get_tweet : ", data)
        self.assertEqual(
            data["payload"],
            self.payload,
        )
        self.assertEqual(
            data["user"],
            self.user.id,
        )

    def test_put_tweet(self):
        response = self.client.put(self.URL_Valid, {
            'payload': self.payload_update,
            "user": self.user.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        print("test_put_tweet :", data)
        self.assertEqual(data["payload"], self.payload_update)

    def test_delete_tweet(self):
        response = self.client.delete(self.URL_Valid)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
