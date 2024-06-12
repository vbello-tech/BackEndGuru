from django.urls import path
from .views import (
    CreateBlogView,
    BlogDetailView,
    BlogListView,
)

app_name = "blog"

urlpatterns = [
    path('create/', CreateBlogView.as_view(), name="create"),
    path('<str:title>/<str:slug>/', BlogDetailView.as_view(), name="detail"),
    path('list/', BlogListView.as_view(), name="list"),
]
