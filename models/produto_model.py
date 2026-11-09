
import sqlite3

BANCO = "database/estoque.db"


# Conectar ao banco
def conectar():
    return sqlite3.connect(BANCO)


# Criar tabela
def criar_tabela():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            valor REAL NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


# Listar produtos
def listar_produtos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")

    produtos = cursor.fetchall()

    conexao.close()

    return produtos


# Criar produtos
def criar_produtos(nome, valor):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO produtos (nome, valor) VALUES (?, ?)",
        (nome, valor)
    )

    conexao.commit()
    conexao.close()


# Deletar produtos
def deletar_produto(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM produtos WHERE id = ?",
        (id,)
    )

    conexao.commit()
    conexao.close()
