from django.shortcuts import render, redirect
from django.http import HttpResponse
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

@login_required
def about(request):
    # if not request.user.is_authenticated: return redirect('login')
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
