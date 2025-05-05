from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Post

def posts_list(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'blog_posts/posts_list.html', {'posts': posts})


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog_posts/post_page.html', {'post': post})


def get_all_posts_json(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        data = [
            {
                'id': post.id,
                'title': post.title,
                'body': post.body,
                'slug': post.slug,
                'date': post.date.isoformat(),
            }
            for post in posts
        ]
        return JsonResponse(data, safe=False)

def get_post_by_id_json(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, id=post_id)
        data = {
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'slug': post.slug,
            'date': post.date.isoformat(),
        }
        return JsonResponse(data)