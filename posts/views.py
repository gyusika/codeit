from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
from django.urls import reverse
from django.shortcuts import redirect
from urllib import request
from .models import Post
from .forms import PostForm
from braces.views import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return redirect('post-list')

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    ordering = ['dt_created']
    paginate_by = 15


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    form_class = PostForm
    raise_exception =  True

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})
    
    def test_func(self, user):
        return self.request.user.is_superuser


class PageDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Post
    raise_exception =  True

    def test_func(self, user):
        post = self.get_object()
        return post.title == self.request.user.username


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    raise_exception =  True

    def get_success_url(self) :
        return reverse('post-detail', kwargs={'pk':self.object.id})
    
    def test_func(self, user):
        return self.request.user.is_superuser

class PageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    raise_exception =  True

    def get_success_url(self):
        return reverse('post-list')
    
    def test_func(self, user):
        return self.request.user.is_superuser