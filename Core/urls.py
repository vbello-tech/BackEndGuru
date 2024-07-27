"""
URL configuration for Core project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Users.urls', namespace="user")),
    path('challenge/', include("Challenges.urls", namespace="challenge")),
    path('blog/', include("Blog.urls", namespace="blog")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('summernote/', include('django_summernote.urls')),
]

handler404 = 'Users.views.handler404'
handler500 = 'Users.views.handler500'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
