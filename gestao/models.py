from typing import Any
from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=256)
    paginas = models.IntegerField()
