from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # get all posts from database
    return render(request, "post_list.html", {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, "post_detail.html", {"post":post})

#class based alternative (only use if complex view required)
'''
class PostList(ListView):
    model = Post
    template_name = "post_list.html"
'''