from database import db

class Missoes(db.Model):
  __tablename__="missao"
  id = db.Column(db.Integer, primary_key=True)
  nome_missao = db.Column(db.String(50), nullable=False)
  data_lancamento = db.Column(db.Date, nullable=False)
  destino = db.Column(db.String(30), nullable=False)
  estado_missao = db.Column(db.String(30), nullable=False)
  tripulacao = db.Column(db.String(60), nullable=False)
  carga_util = db.Column(db.String(60), nullable=False)
  duracao_missao = db.Column(db.String(30), nullable=False)
  custo_missao = db.Column(db.Numeric(10, 2), nullable=False)
  status_missao = db.Column(db.String, nullable=False)
  
  def __init__(self, nome_missao, data_lancamento, destino, estado_missao, tripulacao, carga_util, duracao_missao, custo_missao, status_missao):
    self.nome_missao = nome_missao
    self.data_lancamento = data_lancamento
    self.destino = destino
    self.estado_missao = estado_missao
    self.tripulacao = tripulacao
    self.carga_util = carga_util
    self.duracao_missao = duracao_missao
    self.custo_missao = custo_missao
    self.status_missao = status_missao