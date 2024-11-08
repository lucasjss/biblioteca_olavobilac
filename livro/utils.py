import requests
from .models import Livros

import requests
from livro.models import Livros


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
            capa_url = volume_info.get("imageLinks", {}).get("thumbnail", "")
            descricao = volume_info.get("description", "Descrição não disponível")

            # Verificar se o livro já existe no banco
            if not Livros.objects.filter(nome=nome).exists():
                livro = Livros(
                    nome=nome,
                    autor=autores[0],
                    co_autor=autores[1] if len(autores) > 1 else "",
                    disponivel=False,  # Definido como indisponível por padrão
                    exemplares=0,  # Definido como 0 exemplares por padrão
                    capa_url=capa_url,  # Adiciona a URL da capa
                    descricao=descricao,  # Adiciona a sinopse do livro
                )
                livro.save()
                print(f"Livro '{nome}' salvo com sucesso.")
            else:
                print(f"Livro '{nome}' já existe no banco de dados.")
    else:
        print("Erro ao acessar a API do Google Books:", response.status_code)


def importar_todos_livros_google():
    """
    Busca todos os livros da API do Google Books e salva no banco de dados.
    """
    url_base = "https://www.googleapis.com/books/v1/volumes?q=*"
    start_index = 0
    max_results = 40  # Máximo de 40 resultados por vez
    livros_importados = 0

    while True:
        url = f"{url_base}&startIndex={start_index}&maxResults={max_results}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            # Caso não haja mais livros, parar a execução
            if not data.get("items"):
                break

            for item in data.get("items", []):
                volume_info = item.get("volumeInfo", {})
                nome = volume_info.get("title", "Título Desconhecido")
                autores = volume_info.get("authors", ["Autor Desconhecido"])
                capa_url = volume_info.get("imageLinks", {}).get("thumbnail", "")
                descricao = volume_info.get("description", "Descrição não disponível")

                # Verificar se o livro já existe no banco
                if not Livros.objects.filter(nome=nome).exists():
                    livro = Livros(
                        nome=nome,
                        autor=autores[0],
                        co_autor=autores[1] if len(autores) > 1 else "",
                        disponivel=False,  # Definido como indisponível (False)
                        exemplares=0,  # Definido como 0 exemplares
                        capa_url=capa_url,  # Adiciona a URL da capa
                        descricao=descricao,  # Adiciona a sinopse
                    )
                    livro.save()
                    livros_importados += 1
                    print(f"Livro '{nome}' salvo com sucesso.")
                else:
                    print(f"Livro '{nome}' já existe no banco de dados.")

            # Atualizar o índice para buscar os próximos livros
            start_index += max_results  # Atualiza o índice para buscar a próxima página
        else:
            print(f"Erro ao acessar a API do Google Books: {response.status_code}")
            break

    print(f"{livros_importados} livros foram importados com sucesso.")
