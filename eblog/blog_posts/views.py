from django.shortcuts import render
from .models import Post

def posts_list(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'blog_posts/posts_list.html', { 'posts': posts})


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog_posts/post_page.html', {'post': post})