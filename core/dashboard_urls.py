from django.urls import path
from . import dashboard_views

app_name = 'dashboard'

urlpatterns = [
    # Notice Management
    path('notices/', dashboard_views.notice_list, name='notice_list'),
    path('notices/add/', dashboard_views.add_notice, name='add_notice'),
    path('notices/edit/<int:pk>/', dashboard_views.edit_notice, name='edit_notice'),
    path('notices/delete/<int:pk>/', dashboard_views.delete_notice, name='delete_notice'),
]
