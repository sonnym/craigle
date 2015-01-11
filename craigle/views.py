from itertools import groupby

from django.shortcuts import render

from posts.models import Post, DatedPosts

def home(request):
    posts = Post.objects.exclude(posted_at=None).order_by('-posted_at')[:250]
    posts_by_date = [DatedPosts(date, list(posts)) for date, posts in groupby(posts, lambda post: post.posted_at_date)]

    return render(request, 'home.html', { 'posts_by_date': sorted(posts_by_date) })
