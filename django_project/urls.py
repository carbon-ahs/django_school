# Gemini
# django_project/urls.py

from django.contrib import admin
from django.urls import path, include, re_path # Import re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve # Import the serve view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]

# Serve static and media files in development (when DEBUG is True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Also add for static if not already present

# Serve media and static files in production (when DEBUG is False)
# This uses Django's built-in serve view, which WhiteNoise then handles
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]

    # from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", include("core.urls")),
# ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# # This block is crucial for serving media in development
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)