from django.shortcuts import render
from models import Post
from django.views.generic import ListView
from django.views.generic.edit import FormView
from forms import PostForm


class lists(ListView):
    model = Post


class PostFormView(FormView):
    template_name = 'blog/form.html'
    form_class = PostForm
    success_url = '/blogs/lists'
