# Blog

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



