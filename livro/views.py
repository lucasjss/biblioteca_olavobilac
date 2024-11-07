from django.http import HttpResponse
from django.shortcuts import render
from .models import Livros
from django.db.models import Q
from django.shortcuts import get_object_or_404


# Create your views here.


def lista_livros(request):
    termo_pesquisa = request.GET.get("search", "")
    categoria_filtro = request.GET.get("categoria", "")
    autor_filtro = request.GET.get("autor", "")

    livros = Livros.objects.all()

    if termo_pesquisa:
        livros = livros.filter(nome__icontains=termo_pesquisa)
    if categoria_filtro:
        livros = livros.filter(categoria__icontains=categoria_filtro)
    if autor_filtro:
        livros = livros.filter(
            Q(autor__icontains=autor_filtro) | Q(co_autor__icontains=autor_filtro)
        )

    context = {
        "livros": livros,
        "termo_pesquisa": termo_pesquisa,
        "categoria_filtro": categoria_filtro,
        "autor_filtro": autor_filtro,
    }
    return render(request, "livros.html", context)


def detalhes_livro(request, livro_id):
    livro = get_object_or_404(Livros, id=livro_id)
    return render(request, "detalhes_livro.html", {"livro": livro})


def home(request):
    return render(request, "home.html")


def registrar(request):
    return "html"
