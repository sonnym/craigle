from django.shortcuts import render

from posts.models import Post

def home(request):
    posts = Post.objects.exclude(title='').order_by('-posted_at')[:250]

    return render(request, 'home.html', { 'posts': posts })
