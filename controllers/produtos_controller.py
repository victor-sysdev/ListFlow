from flask import Blueprint, render_template, request, redirect , url_for
from models.produto_model import listar_produtos, criar_produtos, deletar_produto

produtos_bp = Blueprint("produtos", __name__)

@produtos_bp.route("/")
def index():
    produtos = listar_produtos()

    return render_template(

        "index.html",
        produtos=produtos

    )

@produtos_bp.route("/criar", methods=["GET", "POST"])
def criar(): 

    if request.method == "POST":

        nome = request.form["nome"]
        valor = request.form["valor"]

        criar_produtos(nome, valor)

        return redirect(url_for("produtos.index"))

    return render_template("formulario.html")

# Deletar produtos
@produtos_bp.route("/deletar/<int:id>", methods=["POST"])
def deletar(id):

    deletar_produto(id)

    return redirect(url_for("produtos.index"))

