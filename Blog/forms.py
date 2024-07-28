from django import forms
from .models import Blog, Comment
from django_summernote.widgets import SummernoteWidget


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ("author", "publish_date", "slug",)

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'post_image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'body': SummernoteWidget(
                attrs={
                    'class': 'form-control',
                }
            )
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'Input your comment here',
                    'rows': 5,
                    'cols': 80,
                }
            )

        }
