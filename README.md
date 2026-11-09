📦 ListFlow
Sistema de gerenciamento de produtos e controle de estoque

O ListFlow é uma aplicação web desenvolvida em Python utilizando Flask e SQLite. Seu objetivo é facilitar o gerenciamento de produtos, permitindo cadastrar, visualizar e excluir itens de um estoque através de uma interface simples, moderna e intuitiva.

🚀 Tecnologias utilizadas
Python 3.14 — Linguagem de programação.
Flask — Framework web para Python.
SQLite3 — Banco de dados relacional.
HTML5 — Estrutura das páginas.
CSS3 — Estilização e responsividade.
Jinja2 — Renderização dinâmica de páginas HTML.
✨ Funcionalidades
Cadastro de produtos.
Listagem de produtos.
Exclusão de produtos.
Armazenamento de dados com SQLite.
Dashboard para visualização do estoque.
Interface personalizada e responsiva.
Edição de produtos.
Pesquisa de produtos.
Relatório de estoque.
📁 Estrutura do projeto
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

⚙️ Como executar o projeto
1. Clone o repositório
bash
git clone URL_DO_REPOSITORIO

2. Entre na pasta
bash
cd ListFlow

3. Instale as dependências
bash
pip install Flask

4. Execute a aplicação
bash
python app.py

5. Acesse no navegador
text
http://127.0.0.1:5000/

🗄️ Banco de dados

O projeto utiliza SQLite3 para armazenar os produtos.

A tabela produtos possui os seguintes campos:

Campo	Tipo	Descrição
id	INTEGER	Identificador único
nome	TEXT	Nome do produto
valor	REAL	Valor do produto

A tabela é criada automaticamente quando a aplicação é iniciada.

🎨 Interface

O ListFlow possui uma interface moderna com:

Tema escuro.
Identidade visual personalizada.
Detalhes em roxo e azul.
Dashboard de produtos.
Formulário de cadastro.
Layout responsivo.
🎯 Objetivo do projeto

O ListFlow foi desenvolvido como projeto de aprendizado e prática de desenvolvimento web com Python, explorando conceitos como:

Desenvolvimento de aplicações web com Flask.
Arquitetura MVC (Models e Controllers).
Operações CRUD.
Integração com banco de dados SQLite.
Criação de interfaces com HTML e CSS.
Organização e estruturação de projetos Python.
📌 Próximas melhorias
Implementar edição de produtos.
Adicionar sistema de pesquisa.
Criar controle de quantidade em estoque.
Implementar autenticação de usuários.
Adicionar relatórios e indicadores.

Desenvolvido com Python, Flask e SQLite.

ListFlow — Organize seus produtos. Simplifique sua gestão.