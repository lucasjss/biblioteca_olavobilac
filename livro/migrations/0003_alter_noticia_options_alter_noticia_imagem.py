# Generated by Django 5.1.2 on 2024-11-11 14:22

import livro.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0002_noticia'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noticia',
            options={'verbose_name_plural': 'Notícias'},
        ),
        migrations.AlterField(
            model_name='noticia',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='noticias/', validators=[livro.models.validate_square_image]),
        ),
    ]
