ListFlow

Sistema de gerenciamento de produtos e controle de estoque.

O ListFlow é uma aplicação web desenvolvida com Python e Flask, que permite gerenciar produtos de maneira simples e organizada.

Sobre o projeto

O objetivo do projeto é desenvolver um sistema de controle de produtos, utilizando operações CRUD e armazenamento de dados com SQLite.

Tecnologias utilizadas
Python 3.14
Flask
SQLite3
HTML5
CSS3
Jinja2
Git e GitHub
Funcionalidades
Cadastro de produtos.
Listagem de produtos.
Exclusão de produtos.
Armazenamento de dados no SQLite.
Dashboard personalizado.
Interface responsiva.
Estrutura do projeto
text
ListFlow/
│
├── app.py
│
├── controllers/
│   └── produtos_controller.py
│
├── models/
│   └── produto_model.py
│
├── database/
│   └── estoque.db
│
├── templates/
│   ├── index.html
│   └── formulario.html
│
└── README.md

Como executar o projeto

1. Clone o repositório

bash
git clone https://github.com/victor-sysdev/ListFlow.git


2. Entre na pasta

bash
cd ListFlow


3. Instale o Flask

bash
pip install Flask


4. Execute a aplicação

bash
python app.py


5. Acesse no navegador

http://127.0.0.1:5000/

Banco de dados

O projeto utiliza SQLite3.

A tabela produtos possui três campos:

id: identificador do produto.
nome: nome do produto.
valor: preço do produto.

A tabela é criada automaticamente pela aplicação.

Melhorias futuras
Edição de produtos.
Pesquisa de produtos.
Controle de quantidade.
Relatórios de estoque.
Autenticação de usuários.
Desenvolvedor

Victor Merencio

GitHub: victor-sysdev

ListFlow — Organize seus produtos. Simplifique sua gestão.
