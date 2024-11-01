import requests
from .models import Livros


def importar_livros_google(termo_pesquisa):
    """
    Busca livros da API do Google Books e salva no banco de dados.

    :param termo_pesquisa: O termo a ser pesquisado na API.
    """
    url = f"https://www.googleapis.com/books/v1/volumes?q={termo_pesquisa}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for item in data.get("items", []):
            volume_info = item.get("volumeInfo", {})
            nome = volume_info.get("title", "Título Desconhecido")
            autores = volume_info.get("authors", ["Autor Desconhecido"])
            categoria = volume_info.get("categories", ["Categoria Desconhecida"])[0]
            capa_url = volume_info.get("imageLinks", {}).get("thumbnail", "")

            # Verificar se o livro já existe no banco
            if not Livros.objects.filter(nome=nome).exists():
                livro = Livros(
                    nome=nome,
                    autor=autores[0],
                    co_autor=autores[1] if len(autores) > 1 else "",
                    disponível=True,  # Definido como disponível por padrão
                    exemplares=1,  # Exemplo de valor inicial de exemplares
                    categoria=categoria,
                    capa_url=capa_url,  # Adiciona a URL da capa
                )
                livro.save()
                print(f"Livro '{nome}' salvo com sucesso.")
            else:
                print(f"Livro '{nome}' já existe no banco de dados.")
    else:
        print("Erro ao acessar a API do Google Books:", response.status_code)
