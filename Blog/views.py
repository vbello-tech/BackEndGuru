from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from .models import Blog
from .forms import CreateBlogForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class CreateBlogView(CreateView, LoginRequiredMixin):
    """
    View to create blog article
    """
    model = Blog
    template_name = "blog/create.html"
    form_class = CreateBlogForm

    def get_success_url(self):
        return reverse("blog:detail", kwargs={
            'slug': self.object.slug,
            'title': self.object.title,
        })

    # save authenticated user if form is valid
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogDetailView(DetailView):
    """
    View for blog detail
    """
    model = Blog
    template_name = 'blog/detail.html'
    context_object_name = "blog"


class BlogListView(ListView):
    """
    View for all blog list
    """
    model = Blog
    context_object_name = "blogs"
    template_name = "blog/list.html"

    # Queryset to render all blog from db in order of publish_date (newest first)
    def get_queryset(self):
        return Blog.objects.order_by('-publish_date')
