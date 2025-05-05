from django.urls import path
from . import views

app_name = 'blog_posts'

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('<slug:slug>', views.post_page, name="page"),
    path('api/posts/', views.get_all_posts_json, name='get_all_posts_json'),
    path('api/posts/<int:post_id>/', views.get_post_by_id_json, name='get_post_by_id_json'),
]