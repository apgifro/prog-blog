from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.contrib.auth.views import LogoutView, LoginView

from app.forms import EmailPost, ComentModelForm, CadUsuarioForm
from app.models import Post, Comentario

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin


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


class ComentarioCreateView(LoginRequiredMixin, CreateView):
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


class CadUsuarioView(CreateView):
    template_name = 'blog/usuarios/cadusuario.html'
    form_class = CadUsuarioForm
    success_url = reverse_lazy('loginuser')

    def form_valid(self, form):
        form.cleaned_data
        form.save()
        messages.success(self.request, 'Usuário cadastrado!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Usuário não cadastrado.')
        return super().form_invalid(form)


class LoginUsuarioView(LoginView):
    template_name = 'blog/usuarios/login.html'
    model = User
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        nome = form.cleaned_data['username']
        senha = form.cleaned_data['password']
        usuario = authenticate(self.request, username=nome, password=senha)

        if usuario is not None:
            login(self.request, usuario)
            return redirect('home')
        messages.error(self.request, 'Usuário inexistente.')
        return redirect('loginuser')

    def form_invalid(self, form):
        messages.error(self.request, 'Não foi possível fazer login.')
        return redirect('loginuser')


class LogoutView(LoginRequiredMixin, LogoutView):

    def get(self, request):
        logout(request)
        return redirect('home')