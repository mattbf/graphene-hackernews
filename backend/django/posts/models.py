from django.db import models


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_published_at = models.DateTimeField("date published")
    post_url = models.URLField()
    votes = models.IntegerField(default=0)
