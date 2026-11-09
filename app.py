
from flask import Flask
from controllers.produtos_controller import produtos_bp
from models.produto_model import criar_tabela

app = Flask(__name__)

# Criar tabela do banco
criar_tabela()

# Registrar rotas
app.register_blueprint(produtos_bp)

if __name__ == "__main__":
    app.run(debug=True)
