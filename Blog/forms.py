from django import forms
from .models import Blog
from ckeditor.widgets import CKEditorWidget


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
            'body': CKEditorWidget(
                attrs={
                    'class': 'form-control',
                }
            )
        }
