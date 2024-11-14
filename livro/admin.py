from django.contrib import admin
from .models import Livros, Noticia

# Register your models here.

admin.site.register(Livros)


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "data_publicacao")
    search_fields = ("titulo", "conteudo")
