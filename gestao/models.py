from typing import Any
from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=256)
    email = models.EmailField()

class Livro(models.Model):
    titulo = models.CharField(max_length=256)
    paginas = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
