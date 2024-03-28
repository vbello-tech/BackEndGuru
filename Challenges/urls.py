from django.urls import path
from .views import (
    CreateChallengeView,
    ChallengeListView,
    ChallengeDetailView,
    create_entry,
    EntryDetailView,
    SubmitEntryView,
    ChallengeLevelView,
)

app_name = "challenge"

urlpatterns = [
    path('create/', CreateChallengeView.as_view(), name="create"),
    path('all-challenge/', ChallengeListView.as_view(), name="list"),
    path('<str:title>/<str:id>/', ChallengeDetailView.as_view(), name="detail"),
    path('take-challenge/', create_entry, name="take_entry"),
    path('entry/detail/<str:slug>/', EntryDetailView.as_view(), name="entry_detail"),
    path('entry/<str:slug>/submit/', SubmitEntryView.as_view(), name="submit_entry"),
    path('<str:level>/', ChallengeLevelView.as_view(), name="level"),
]


