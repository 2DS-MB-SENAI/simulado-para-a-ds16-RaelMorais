from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
        telefone = models.CharField(max_length=255, null=True, blank=True, default="0")
        escolaridade = models.CharField(max_length=255, null=True, blank=True)
        REQUIRED_FIELDS = ['telefone']

        def __str__(self):
            return self.username
# Create your models here.
