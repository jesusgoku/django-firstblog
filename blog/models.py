from __future__ import unicode_literals

from django.utils import timezone

from django.db import models

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __srt__(self):
        return self.title

    def __unicode__(self):
        return self.title
