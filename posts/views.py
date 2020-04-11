from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .models import Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content')
    success_url = reverse_lazy('index')


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
