# Generated by Django 4.2rc1 on 2023-04-06 00:13

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='posts', variations={'thumb': {'cropt': True, 'height': 438, 'width': 438}}, verbose_name='Imagem'),
        ),
    ]
