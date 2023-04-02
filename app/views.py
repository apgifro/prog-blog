from django.views.generic import ListView
from django.views.generic import TemplateView

from app.models import Post


class Index(ListView):
    context_object_name = 'posts'
    template_name = 'blog/index.html'
    queryset = Post.publicados.all()


class PostView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        queryset = Post.publicados.get(slug=kwargs['slug'])
        context.update({'item': queryset})
        return context

    context_object_name = 'item'
    template_name = "blog/post/post_detail.html"
