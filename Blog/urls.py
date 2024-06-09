from django.urls import path
from .views import (
    CreateBlogView,
    BlogDetailView
)

app_name = "blog"

urlpatterns = [
    path('create/', CreateBlogView.as_view(), name="create_blog"),
    path('<str:title>/<str:slug>/', BlogDetailView.as_view(), name="blog_detail"),
]
