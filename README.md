# Blog

## 2023-04-26

### Comentários

![screen](/readme/imgt.png)

## 2023-04-12 e 2023-04-19

Compartilhar post por e-mail.

![screen](/readme/2023-04-12.png)

![screen](/readme/2023-04-12.2.png)

forms.py
```
class EmailPost(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    destino = forms.EmailField()
    coments = forms.CharField(required=False,
                              widget=forms.Textarea)

    def enviar_email(self, post):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        destino = self.cleaned_data['destino']
        coments = self.cleaned_data['coments']

        conteudo = f'Recomendo ler o post: {post.titulo}\n' \
                   f'Comentários: {coments}'
        mail = EmailMessage(
            subject=f"{nome} recomenda este post!",
            body=conteudo,
            from_email='contato@meublog.com.br',
            to=[destino],
            headers={'Reply-To': email}
        )
        mail.send()
```

urls.py
```
path('share/<int:pk>/', FormContactView.as_view(), name='share'),
```

views.py
```
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
        messages.success(self.request, f'Post: {meupost.titulo}'
                                       f'enviado com sucesso.')
        return super(FormContactView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        meupost = self.get_context_data()['post']
        messages.error(self.request, f'Post: {meupost.titulo}'
                                       f'não enviado.')
        return super(FormContactView, self).form_valid(form, *args, **kwargs)
```

Criar share.html

Adicionar em detail.html
```
<p>
    <a href="{% url 'share' detail.id %}">
    Compartilhar por e-mail...
    </a>
</p>
```

## 2023-04-05

Paginação

![screen](/readme/2023-04-0501.png)

![screen](/readme/2023-04-0502.png)

![screen](/readme/2023-04-0503.png)


Truncate

```
{{ item.corpo|truncatewords:30|linebreaks }}
```

Como fazer paginação?

Adicionar na view

```
paginate_by = 3
```

Criar HTML de paginação
```
<span>
    {% if page.has_previous %}
      <a href="?page={{ page.previous_page_number }}">&#9664;</a>
    {% endif %}
    
    <span>
      Página {{ page.number }} de {{ page.paginator.num_pages }}
    </span>
    
    {% if page.has_next %}
      <a href="?page={{ page.next_page_number }}">&#9654;</a>
    {% endif %}
</span>
```

Incluir HTML na página e pronto!
```
{% include 'blog/base/paginacao.html' with page=page_obj %}
```

## 2023-04-01

Adicionar herança de template.

![screen](/readme/posts_view.png)

![screen](/readme/post_detail.png)

## 2023-03-29

Instalar dependências e iniciar.

```
pip install django==4.2rc1
django-admin startproject blog .
```

Configurar `settings.py`.

Configurar `urls.py`.

Criar `models.py`.

```
python manage.py makemigrations
python manage.py migrate
```

```
python manage.py createsuperuser
```

Criar `admin.py`.

```
python manage.py shell

from app.models import Post

novo = Post(titulo='Post no shell', 
            slug='post-no-shell', 
            corpo='corpo', 
            status='publicado', 
            autor=usuarios[0])
novo.save()

posts = Post.objects.all()
posts = Post.objects.last()
posts = Post.objects.first()
post = Post.objects.get(titulo='Post no shell')
posts = Post.objects.filter(status='rascunho')
```

Criar gerenciador `models.Manager` em `models.py`

Criar `views.py`

Criar `listarposts.html`

Ajustar `urls.py`

![screen1](/readme/blog.png)



