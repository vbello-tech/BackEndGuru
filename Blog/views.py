from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import Blog
from .forms import CreateBlogForm
from django.urls import reverse


# Create your views here.

class CreateBlogView(CreateView):
    model = Blog
    template_name = "blog/create.html"
    form_class = CreateBlogForm

    def get_success_url(self):
        return reverse("blog:blog_detail", kwargs={
            'slug': self.object.slug,
            'title': self.object.title,
        })

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    context_object_name = "blog"
