from django import forms
from .models import Blog


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
            'description': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'post_image': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'body': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }
