from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Página principal
    path("livros/", views.cadastrar, name="livros"),
    path("noticias/", views.cadastrar, name="noticias"),
]
