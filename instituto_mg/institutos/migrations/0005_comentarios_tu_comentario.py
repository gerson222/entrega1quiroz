# Generated by Django 4.0.6 on 2022-09-07 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutos', '0004_alter_comentarios_seleccionar_curso_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='Tu_comentario',
            field=models.CharField(default='some_value', max_length=50),
        ),
    ]
