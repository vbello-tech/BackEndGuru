from django.contrib import admin
from .models import Challenge, ChallengeEntry
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.


class ChallengenAdmin(SummernoteModelAdmin):
    summernote_fields = ('features',)
    list_display = ['title', ]


admin.site.register(Challenge, ChallengenAdmin)


@admin.register(ChallengeEntry)
class ChallengenEntryAdmin(admin.ModelAdmin):
    list_display = ['participant', 'challenge', 'completed', ]
