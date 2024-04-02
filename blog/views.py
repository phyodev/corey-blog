from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def home(request):
    # if not request.user.is_authenticated: return redirect('login')
    context = {
        'posts': Post.objects.all(),
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post' # no need to declare template_name   default is  <app>/<model>_<viewtype>.html

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required
def about(request):
    # if not request.user.is_authenticated: return redirect('login')
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
