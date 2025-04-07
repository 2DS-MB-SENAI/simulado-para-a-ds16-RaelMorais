from django.db import models

from django.db import models

class Autores(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField(default='0')
    biografia = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255, default='0')
    paginas = models.PositiveIntegerField()
    
    def __str__(self):
        return self.titulo


# Create your models here.

