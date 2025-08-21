from django.urls import path
from . import dashboard_views

app_name = 'dashboard'

urlpatterns = [
    # Notice Management
    path('notices/', dashboard_views.admin_notice_list, name='admin_notice_list'),
    path('notices/add/', dashboard_views.admin_add_notice, name='admin_add_notice'),
    path('notices/edit/<int:pk>/', dashboard_views.admin_edit_notice, name='admin_edit_notice'),
    path('notices/delete/<int:pk>/', dashboard_views.admin_delete_notice, name='admin_delete_notice'),
]
