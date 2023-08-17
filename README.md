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
Acesse http://127.0.0.1:5000/ em seu navegador para ver a página de filmes.
##Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um PR para melhorias, correções de bugs ou novas funcionalidades.

## Estrutura

`app.py`: Contém o código do servidor Flask que cria a API e renderiza a página web.\n

`netflix_db.sqlite`: Banco de dados SQLite contendo os dados dos filmes da Netflix.

`templates/index.html`: Página web interativa que consome a API e exibe os dados.

`static/styles.css`: Arquivo CSS para estilizar a página.

## Contato
Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

- Email: luana.santana@fatecitapetininga.edu.br
- Site: [https://linktr.ee/LuanaCS](https://linktr.ee/LuanaCS)
