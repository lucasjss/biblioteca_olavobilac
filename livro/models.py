from django.core.exceptions import ValidationError
from django.db import models
from PIL import Image


from django.core.exceptions import ValidationError
from django.db import models
from PIL import Image


def validate_square_image(image):
    img = Image.open(image)
    width, height = img.size

    if width != height:
        raise ValidationError("A imagem deve ser quadrada (proporção 1:1).")

    if width != 500 or height != 500:
        raise ValidationError("A imagem deve ter exatamente 500x500 pixels.")


def home(request):
    noticias = Noticia.objects.all().order_by("-data_publicacao")[:3]
    return render(request, "home.html", {"noticias": noticias})


# Create your models here.
class Livros(models.Model):
    nome = models.CharField(max_length=80)
    autor = models.CharField(max_length=50)
    co_autor = models.CharField(max_length=50, blank=True)
    disponivel = models.BooleanField(default=False)
    exemplares = models.FloatField(default=0)
    capa_url = models.URLField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Livro"

    def __str__(self):
        return self.nome


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(
        upload_to="noticias/", blank=True, null=True, validators=[validate_square_image]
    )

    class Meta:
        verbose_name_plural = "Notícias"

    def __str__(self):
        return self.titulo
