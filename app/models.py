from database import db

class Missoes(db.model):
  __tablename__="missão"
  id = db.Column(db.integer, primary_key=True)
  nome_missao = db.Column(db.string(50), nullable=False)
  data_lancamento = db.Column(db.Date, nullable=False)
  destino = db.Column(db.string(30), nullable=False)
  estado_missao = db.Column(db.string(30), nullable=False)
  tripulacao = db.Column(db.string(60), nullable=False)
  carga_util = db.Column(db.string(60), nullable=False)
  duracao_missao = db.Column(db.string(30), nullable=False)
  custo_missao = db.Column(db.numeric(10, 2), nullable=False)
  status_missao = db.Column(db.text, nullable=False)
  