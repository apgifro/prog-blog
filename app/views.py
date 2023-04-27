from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, FormView, CreateView

from app.forms import EmailPost, ComentModelForm
from app.models import Post, Comentario


class Index(ListView):
    context_object_name = 'posts'
    template_name = 'blog/index.html'
    queryset = Post.publicados.all()
    paginate_by = 3


class PostDetailView(DetailView):
    template_name = "blog/post/detail.html"
    context_object_name = 'detail'
    queryset = Post.publicados.all()

    def _get_coments(self, id_post):
        try:
            coments = Comentario.objects.filter(post_id=id_post, status=True)
            return coments
        except Comentario.DoesNotExist:
            return Exception

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = self._get_coments(self.object.id)
        return context


class FormContactView(FormView):
    template_name = 'blog/post/share.html'
    form_class = EmailPost
    success_url = reverse_lazy('home')
    meupost = Post()

    def get_post(self, id_post):
        try:
            return Post.publicados.get(pk=id_post)
        except Post.DoesNotExist:
            messages.error(self.request, 'O post não existe!')
            reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(FormContactView, self).get_context_data(**kwargs)
        context['post'] = self.get_post(self.kwargs['pk'])
        return context

    def form_valid(self, form, *args, **kwargs):
        meupost = self.get_context_data()['post']
        form.enviar_email(meupost)
        messages.success(self.request, f'{meupost.titulo} enviado com sucesso.')
        return super(FormContactView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        meupost = self.get_context_data()['post']
        messages.error(self.request, f'{meupost.titulo} não enviado.')
        return super(FormContactView, self).form_valid(form, *args, **kwargs)


class ComentarioCreateView(CreateView):
    template_name = 'blog/post/comentarios.html'
    form_class = ComentModelForm
    # form_class = forms.ModelForm(model=Comentario, fields=[])

    def _get_post(self, id_post):
        try:
            print(id_post)
            post = Post.publicados.get(id=id_post)
            return post
        except Post.DoesNotExist:
            return Exception

    def form_valid(self, form, *args, **kwargs):
        post = self._get_post(self.kwargs['pk'])
        form.salvar_comentario(post)
        return redirect('detail', post.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self._get_post(self.kwargs['pk'])
        return context


