from django.db import models
from django.conf import settings
import uuid


# history
class History(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    video_id = models.CharField(max_length=200, blank=False)
    video_url = models.CharField(max_length=200, blank=False)


# bookmarks
class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    video_id = models.CharField(max_length=200, blank=False)
    video_url = models.CharField(max_length=200, blank=False)