from django.contrib import admin
from .models import Tweet, Like


class WordFilter(admin.SimpleListFilter):
    title = "Filter by word"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [("elon musk", "Include Elon Musk"),
                ("not_elon musk", "exclude Elon Musk")]

    def queryset(self, request, posts):
        word = self.value()

        if word is not None and "not" in word:
            print(word)
            print(type(word))
            word = word.replace("not_", "")
            return posts.exclude(payload__contains=word)
        elif word:
            return posts.filter(payload__contains=word)
        else:
            posts


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "payload",
        "user",
        "like_count",
    )
    list_filter = ("created_at", WordFilter)
    search_fields = (
        "payload",
        "user__username",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "tweet",
    )
    list_filter = ("created_at", )
    search_fields = ("user__username", )
