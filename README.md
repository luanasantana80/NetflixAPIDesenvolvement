# API de Filmes da Netflix

Este projeto consiste em uma aplicação web que utiliza o framework Flask para criar uma API que lista informações de filmes da Netflix a partir de um banco de dados SQLite. Além disso, a aplicação inclui uma página web interativa que se comunica com a API, permitindo a visualização da lista de todos os filmes e a busca por filmes similares.

## Funcionalidades

- API que lista todos os filmes da Netflix a partir de um banco de dados SQLite.
- Página web interativa que consome a API para exibir a lista de filmes.
- Busca por filmes similares a partir do título de um filme.
- Utiliza Bootstrap para um design moderno e responsivo.

## Pré-requisitos

- Python 3.x
- Bibliotecas: Flask, pandas, sqlite3

## Como Usar

1. Clone este repositório para sua máquina.
2. Certifique-se de que os arquivos `netflix_db.sqlite` e `app.py` estão no mesmo diretório.
3. Abra o terminal e navegue até o diretório do projeto.
4. Execute o servidor Flask com o comando:

   ```bash
   python app.py
