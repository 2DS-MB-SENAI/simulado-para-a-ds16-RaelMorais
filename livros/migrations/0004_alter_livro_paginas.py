# Generated by Django 5.2 on 2025-04-07 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_rename_livros_livro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='paginas',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
