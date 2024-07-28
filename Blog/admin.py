from django.contrib import admin
from .models import Blog, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ('title', 'slug',)


admin.site.register(Blog, BlogAdmin)


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', ]
