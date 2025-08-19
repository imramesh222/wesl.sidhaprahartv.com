from django.urls import path
from .api_views import NoticeListAPIView, NoticeDetailAPIView

urlpatterns = [
    path('notices/', NoticeListAPIView.as_view(), name='notice-list'),
    path('notices/<int:pk>/', NoticeDetailAPIView.as_view(), name='notice-detail'),
]
