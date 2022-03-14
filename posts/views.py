from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
from django.urls import reverse
from urllib import request
from .models import Post
from .forms import PostForm

class IndexRedirectView(RedirectView):
    pattern_name = 'post-list'

class PostListView(ListView):
    model = Post
    ordering = ['dt_created']
    paginate_by = 6

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

class PageDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    def get_success_url(self) :
        return reverse('post-detail', kwargs={'pk':self.object.id})

class PageDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('post-list')