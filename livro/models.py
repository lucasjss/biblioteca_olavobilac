from django.db import models

# Create your models here.


class Livros(models.Model):
    nome = models.CharField(max_length=80)
    autor = models.CharField(max_length=50)
    co_autor = models.CharField(max_length=50, blank=True)
    disponível = models.BooleanField(default=True)
    exemplares = models.FloatField(default=1)
    categoria = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Livro"

    def __str__(self):
        return self.nome
