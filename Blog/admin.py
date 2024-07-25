from django.contrib import admin
from .models import Blog, Comment


# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', ]


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', ]
