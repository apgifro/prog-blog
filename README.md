# Blog

## Passo a passo

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