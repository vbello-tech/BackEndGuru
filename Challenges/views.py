from django.shortcuts import render, redirect, get_object_or_404
from .models import Challenge, ChallengeEntry
from django.views.generic import CreateView, View, ListView
from django.urls import reverse
from .forms import CreateChallengeForm, SubmitEntryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.utils import timezone


class CreateChallengeView(CreateView, LoginRequiredMixin):
    model = Challenge
    form_class = CreateChallengeForm
    template_name = "Challenge/create.html"

    def get_success_url(self):
        return reverse("challenge:detail", kwargs={
            'id': self.object.id,
            'title': self.object.title,
        })

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ChallengeListView(ListView):
    model = Challenge
    context_object_name = "challenges"
    template_name = "Challenge/list.html"

    def get_queryset(self):
        return Challenge.objects.order_by('-created_date')


class ChallengeDetailView(View):
    def get(self, request, id, title, *args, **kwargs):
        challenge = Challenge.objects.prefetch_related('entry_task').get(pk=id)
        entries = challenge.entry_task.filter(completed=True)
        context = {
            'challenge': challenge,
            'entries': entries
        }
        return render(request, 'Challenge/detail.html', context)


def create_entry(request):
    task = get_object_or_404(Challenge, id=request.POST.get('challenge_id'))
    try:
        ChallengeEntry.objects.get(participant=request.user, challenge=task)
        return HttpResponse("You have an entry for this challenge")
    except ObjectDoesNotExist:
        entry = ChallengeEntry.objects.create(
            participant=request.user, challenge=task
        )
        return redirect(entry.get_entry())


class EntryDetailView(View, LoginRequiredMixin):
    def get(self, request, slug, *args, **kwargs):
        entry = ChallengeEntry.objects.get(slug=slug)
        context = {
            'entry': entry,
        }
        return render(request, 'Challenge/entry.html', context)


class SubmitEntryView(View, LoginRequiredMixin):
    def get(self, request, slug, *args, **kwargs):
        entry = get_object_or_404(ChallengeEntry, slug=slug)
        form = SubmitEntryForm()
        context = {
            'entry': entry,
            'form': form,
        }
        return render(request, 'Challenge/submitentry.html', context)

    def post(self, request, slug, *args, **kwargs):
        if self.request.method == "POST":
            entry = get_object_or_404(ChallengeEntry, slug=slug)
            form = SubmitEntryForm(request.POST)
            if form.is_valid():
                entry.description = form.cleaned_data.get('description')
                entry.github = form.cleaned_data.get('github')
                entry.project = form.cleaned_data.get('project')
                entry.completed = True
                entry.datesubmitted = timezone.now()
                entry.save()
                messages.success(request, "You have successfully submitted and closed this entry.")
                return redirect(entry.get_entry())


class ChallengeLevelView(View):
    def get(self, request, level, *args, **kwargs):
        challenges = Challenge.objects.filter(difficulty=level)
        context = {
           'challenges': challenges
        }
        return render(request, 'Challenge/level.html', context)