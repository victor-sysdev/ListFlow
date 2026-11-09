📦 ListFlow
Organize seus produtos. Simplifique sua gestão.

O ListFlow é um sistema web de gerenciamento de produtos desenvolvido com Python e Flask. A aplicação permite cadastrar, visualizar e excluir produtos, utilizando SQLite para armazenar os dados.

O projeto foi desenvolvido com foco no aprendizado de desenvolvimento web, organização de código e operações CRUD.

🖥️ Tecnologias
Tecnologia	Utilização
🐍 Python	Linguagem principal
⚡ Flask	Framework web
🗄️ SQLite	Banco de dados
🌐 HTML5	Estrutura das páginas
🎨 CSS3	Estilização
🔧 Jinja2	Templates dinâmicos
🔀 Git	Controle de versão
✨ Funcionalidades
Cadastro de produtos.
Listagem de produtos.
Exclusão de produtos.
Integração com banco de dados SQLite.
Dashboard personalizado.
Interface moderna com tema escuro.
Layout responsivo.
🔜 Próximas funcionalidades
Editar produtos.
Pesquisar produtos.
Controle de quantidade em estoque.
Cálculo do valor total do estoque.
Sistema de login.
Relatórios de produtos.
📂 Estrutura do projeto
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

⚙️ Instalação e execução
1. Clone o repositório
bash
git clone https://github.com/victor-sysdev/ListFlow.git

2. Acesse a pasta
bash
cd ListFlow

3. Instale as dependências
bash
pip install Flask

4. Execute o projeto
bash
python app.py

5. Acesse no navegador
text
http://127.0.0.1:5000/

🗄️ Banco de dados

O ListFlow utiliza SQLite3 para armazenar os produtos.

A tabela principal é chamada produtos e possui os seguintes campos:

Campo	Tipo	Descrição
id	INTEGER	Identificador único
nome	TEXT	Nome do produto
valor	REAL	Valor do produto

A tabela é criada automaticamente durante a inicialização da aplicação.

🎨 Identidade visual

O ListFlow possui uma interface desenvolvida com:

Tema escuro.
Tons de roxo e azul.
Dashboard intuitivo.
Formulário de cadastro personalizado.
Tabelas para visualização dos produtos.
Design responsivo.
🎯 Objetivo

Este projeto tem como objetivo praticar e desenvolver conhecimentos em:

Python e Flask.
Desenvolvimento de aplicações web.
Operações CRUD (Create, Read, Update e Delete).
Integração com banco de dados SQLite.
Organização de projetos com Models e Controllers.
HTML, CSS e templates Jinja2.
Controle de versão com Git e GitHub.
👨‍💻 Desenvolvedor

Victor Merencio

GitHub: @victor-sysdev

<p align="center">
Desenvolvido com 🐍 Python, ⚡ Flask e 🗄️ SQLite.
</p>

<p align="center">
**ListFlow — Organize seus produtos. Simplifique sua gestão.**
</p>
