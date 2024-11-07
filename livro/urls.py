from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Página principal
    path("livros/", views.lista_livros, name="lista_livros"),
    path("livros/<int:livro_id>/", views.detalhes_livro, name="detalhes_livro"),
    path("noticias/", views.registrar, name="noticias"),
]
