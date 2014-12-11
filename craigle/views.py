from django.shortcuts import render

from posts.models import Post

def home(request):
    posts = Post.objects.order_by('-id')[:100]

    return render(request, 'home.html', { 'posts': posts })
