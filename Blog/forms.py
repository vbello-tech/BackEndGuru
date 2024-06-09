from django import forms
from .models import Blog


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ("author", "publish_date",)
