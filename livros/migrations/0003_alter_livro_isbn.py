# Generated by Django 5.2 on 2025-04-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_alter_livro_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='isbn',
            field=models.CharField(default='0', max_length=255),
        ),
    ]
