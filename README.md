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