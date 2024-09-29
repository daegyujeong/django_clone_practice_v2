from django.db import models


class CommonModel(models.Model):
    """ abstract """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tweet(CommonModel):
    """tweet."""
    payload = models.TextField(max_length=180)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} says {self.payload}'


class Like(CommonModel):
    """tweet like."""
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    tweet = models.ForeignKey('tweets.Tweet', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} likes {self.tweet}'


# Create your models here.
