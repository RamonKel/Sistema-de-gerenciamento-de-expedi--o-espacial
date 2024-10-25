from flask import Flask
from flask_migrate import Migrate
from app.modelos.database import db

# Inicialize o app
app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bdexpedicao.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'AeroSpace01'  # Chave secreta

# Inicialização do SQLAlchemy
db.init_app(app)  # Inicializa o SQLAlchemy com o app
migrate = Migrate(app, db)  # Inicializa o Flask-Migrate

with app.app_context():
    db.create_all()

# Importar as rotas após inicializar o app e db
from app import routes
