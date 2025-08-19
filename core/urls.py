from django.urls import path
from . import views
from .api_views import NoticeListAPIView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('projects/', views.projects, name='projects'),
    path('reports/', views.reports, name='reports'),
    path('downloads/', views.downloads, name='downloads'),
    path('notice/', views.notice, name='notice'),
    path('contact/', views.contact, name='contact'),
    path('clients/', views.clients, name='clients'),
    path('photo/', views.photo, name='photo'),
    path('video/', views.video, name='video'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('key/info/', views.key_info_view, name='key_info_view'),
    
    # API Endpoints
    path('api/notices/', NoticeListAPIView.as_view(), name='api_notices'),
]
