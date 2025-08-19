from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import admin_views
from django.contrib.auth import views as auth_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# API Schema
schema_view = get_schema_view(
   openapi.Info(
      title="WESL API",
      default_version='v1',
      description="API for WESL website",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Django Admin Panel
    path('admin/', admin.site.urls),

    # API Documentation
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # Public/Main Site URLs
    path('', include('core.urls')),

    # API URLs
    path('api/', include('core.api_urls')),

    # Admin Dashboard URLs (app-specific)
    path('dashboard/', include('core.admin_urls')),

    # Authentication URLs
    path('login/', admin_views.admin_login, name='admin_login'),
    path('logout/', admin_views.logout_view, name='logout'),

    # Password Change URLs under dashboard/
    path(
        'dashboard/password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='password_change.html',
            success_url='/dashboard/password_change/done/'
        ),
        name='password_change'
    ),
    path(
        'dashboard/password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'
    ),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
