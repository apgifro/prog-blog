# Blog

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



