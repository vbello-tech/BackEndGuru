from django import forms
from .models import Challenge


class CreateChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        exclude = ("author", "slug", "image", "instructions",)

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'Title of Challenge',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'A brief description of the Challenge',
                    'rows': 5,
                }
            )
        }


class SubmitEntryForm(forms.Form):
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'form-control',
        "placeholder": 'A description of your entry for this challenge. You can type things like your thought process '
                       'for this challenge and resources that helped you .',
        'rows': 5,
    }))
    language = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": 'The programming language used for the project',
    }))
    framework = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": 'The framework used for the project',
    }))
    database = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": 'The database used for the project',
    }))
    github = forms.URLField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": 'Link to challenge github repo',
    }))
    project = forms.URLField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": 'Link to hosted challenge entry.',
    }))
