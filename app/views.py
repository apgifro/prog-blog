from django.shortcuts import render
from django.views.generic import ListView

from app.models import Post


class ListarPostsListView(ListView):
    context_object_name = 'post'
    template_name = 'blog/post/listarposts.html'
    queryset = Post.publicados.all()
