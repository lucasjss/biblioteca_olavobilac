from django.http import HttpResponse
from django.shortcuts import render
from .models import Livros
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import Noticia


# Create your views here.


def lista_noticias(request):
    noticias = Noticia.objects.all().order_by("-data_publicacao")
    return render(request, "noticias.html", {"noticias": noticias})

def detalhes_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, "detalhes_noticia.html", {"noticia": noticia})

def lista_livros(request):
    termo_pesquisa = request.GET.get("search", "")
    autor_filtro = request.GET.get("autor", "")

    livros = Livros.objects.all()

    if termo_pesquisa:
        livros = livros.filter(nome__icontains=termo_pesquisa)
    if autor_filtro:
        livros = livros.filter(autor__icontains=autor_filtro)

    context = {
        "livros": livros,
        "termo_pesquisa": termo_pesquisa,
        "autor_filtro": autor_filtro,
    }
    return render(request, "livros.html", context)

def detalhes_livro(request, livro_id):
    livro = get_object_or_404(Livros, id=livro_id)
    return render(request, "detalhes_livro.html", {"livro": livro})

def home(request):
    ultimas_noticias = Noticia.objects.all().order_by("-data_publicacao")[:3]
    return render(request, "home.html", {"ultimas_noticias": ultimas_noticias})

def registrar(request):
    return "html"

def detalhe_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, "detalhe_noticia.html", {"noticia": noticia})