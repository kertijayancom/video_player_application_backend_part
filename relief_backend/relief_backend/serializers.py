from rest_framework import serializers
from video.models import History, Bookmark

class HistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = History
        fields = ['url', 'video_id', 'video_url', 'created_at']

class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['url', 'video_id', 'video_url', 'created_at']