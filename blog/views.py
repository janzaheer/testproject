from django.shortcuts import render
from models import Post
from django.views.generic import View

class post_list(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'blog/post_list.html', {'posts': posts})
