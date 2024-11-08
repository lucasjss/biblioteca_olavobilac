from django.db import models

# Create your models here.


class Livros(models.Model):
    nome = models.CharField(max_length=80)
    autor = models.CharField(max_length=50)
    co_autor = models.CharField(max_length=50, blank=True)
    disponivel = models.BooleanField(default=False)
    exemplares = models.FloatField(default=0)
    capa_url = models.URLField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)  # Campo para a sinopse

    class Meta:
        verbose_name = "Livro"

    def __str__(self):
        return self.nome
