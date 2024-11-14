from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"),  # Página principal
    path("livros/", views.lista_livros, name="lista_livros"),
    path("livros/<int:livro_id>/", views.detalhes_livro, name="detalhes_livro"),
    path(
        "noticias/", views.lista_noticias, name="noticias"
    ),  # Página com todas as notícias
    path(
        "noticias/<int:id>/", views.detalhe_noticia, name="detalhe_noticia"
    ),  # Nova URL
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
