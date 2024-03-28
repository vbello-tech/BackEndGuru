from django.contrib import admin
from .models import Challenge, ChallengeEntry


# Register your models here.


@admin.register(Challenge)
class ChallengenAdmin(admin.ModelAdmin):
    list_display = ['title', ]


@admin.register(ChallengeEntry)
class ChallengenEntryAdmin(admin.ModelAdmin):
    list_display = ['participant', 'challenge', 'completed', ]

