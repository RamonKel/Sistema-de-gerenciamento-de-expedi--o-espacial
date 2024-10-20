from app import app
from flask import render_template, request, flash, redirect, url_for
from database import db
from app.models import Missoes
from flask_migrate import Migrate
from datetime import datetime

migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/missao/adicionar', methods=['GET', 'POST'])
def adicionar_missao():
  if request.method == 'POST':
    nome_missao = request.form['nome_missao']
    data_lancamento = request.form['data_lancamento']
    destino = request.form['destino']
    estado_missao = request.form['estado_missao']
    tripulacao = request.form['tripulacao']
    carga_util = request.form['carga_util']
    duracao_missao = request.form['duracao_missao']
    try:
      custo_missao = float(request.form['custo_missao'])
    except ValueError:
      flash('Digite um valor válido')
      return redirect(url_for('adicionar_missao'))
    
    status_missao= request.form['status_missao']
    
    nova_missao = Missoes(nome_missao, datetime.strptime(data_lancamento, '%Y-%m-%d'), destino, estado_missao, tripulacao, carga_util, duracao_missao, custo_missao, status_missao)
    db.session.add(nova_missao)
    db.session.commit()
    flash('Missão adicionada com sucesso!')
    return redirect(url_for('visualizar_missoes'))
  
  return render_template("adicionar_missao.html")

@app.route('/missao', methods=['GET', 'POST'])
def visualizar_missao():
  missao = Missoes.query.order_by(Missoes.data_lancamento.desc().all())
  return render_template('visualizar_missoes.html', missao=missao)

@app.route('/missao/editar/<id:int>', methods=['GET', 'POST'])
def editar_missao():
  a = 1
  
      