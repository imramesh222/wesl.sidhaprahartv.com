from rest_framework import generics, permissions
from .models import Notice
from .serializers import NoticeSerializer

class NoticeListAPIView(generics.ListAPIView):
    serializer_class = NoticeSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        # Get only active notices, ordered by publish date (newest first)
        # and limit to 5 most recent notices
        return Notice.objects.filter(
            is_active=True
        ).order_by('-published_at')[:5]

class NoticeDetailAPIView(generics.RetrieveAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [permissions.AllowAny]
