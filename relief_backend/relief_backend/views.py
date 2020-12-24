from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from relief_backend.serializers import HistorySerializer, BookmarkSerializer
from django.core.serializers import serialize
from video.models import History, Bookmark
from rest_framework.pagination import PageNumberPagination
import datetime

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page'
    max_page_size = 1

class HistoryViewSet(viewsets.ModelViewSet):

    queryset = History.objects.all().order_by('created_at')
    serializer_class = HistorySerializer
    pagination_class = LargeResultsSetPagination

class BookmarkViewSet(viewsets.ModelViewSet):

    queryset = Bookmark.objects.all().order_by('created_at')
    serializer_class = BookmarkSerializer

    # make sure only save to database when the video is unique. 
    # if duplicate, change the datetime to the last request
    def create(self, request, *args, **kwargs):
        data = Bookmark.objects.filter(video_id=request.data.get('video_id'))
        if len(data) == 0:
            return super().create(request, *args, **kwargs)
        else:
            # manually update
            obj = data.all().first()
            obj.created_at = datetime.datetime.now()
            obj.save()
            serializer = self.get_serializer(obj)
            return Response(serializer.data)


