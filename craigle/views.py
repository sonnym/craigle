from django.shortcuts import render

from posts.models import Post

def home(request):
    posts = Post.objects.exclude(posted_at=None).order_by('-posted_at')[:250]

    return render(request, 'home.html', { 'posts': posts })
