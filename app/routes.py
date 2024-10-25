from app import app
from flask import render_template, request, flash, redirect, url_for, Blueprint, jsonify
from app.modelos.database import db
from app.modelos.models import Missoes
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
    return redirect(url_for('visualizar_missao'))
  
  return render_template("adicionar_missao.html")


@app.route('/missao/editar/<int:id>', methods=['PUT', 'POST'])
def editar_missao(id):
  missao = Missoes.query.get_or_404(id)
  if request.method == 'POST':
    missao.nome_missao = request.form['nome_missao']
    missao.data_lancamento = datetime.strptime(request.form['data_lancamento'], '%Y-%m-%d').date()
    missao.destino = request.form['destino']
    missao.estado_missao = request.form['estado_missao']
    missao.tripulacao = request.form['tripulacao']
    missao.carga_util = request.form['carga_util']
    missao.duracao_missao = request.form['duracao_missao']
    missao.custo_missao = float(request.form['custo_missao'])
    missao.status_missao = request.form['status_missao']
    
    db.session.commit()
    flash('Missão editada com sucesso!')
    return redirect(url_for('visualizar_missao'))
  
  return render_template("editar_missao.html", missao=missao)
  
@app.route('/missao/deletar/<int:id>', methods=['DELETE'])
def deletar_missao(id):
  missao = Missoes.query.get_or_404(id)
  db.session.delete(missao)
  db.session.commit()
  flash('Missão deletada com sucesso!')
  return redirect(url_for('visualizar_missao'))

@app.route('/missao', methods=['GET'])
def visualizar_missao():
    missoes = Missoes.query.order_by(Missoes.data_lancamento.desc()).all()
    return render_template('visualizar_missao.html', missoes=missoes)

@app.route('/missao/<int:id>', methods=['GET'])
def detalhes_missao(id):
  missao = Missoes.query.get_or_404(id)
  return render_template('detalhes_missao.html', missao=missao)

@app.route('/missao/pesquisar', methods=['GET'])
def pesquisar_missao():
  data_inicial = request.args.get('data_inicial')
  data_final = request.args.get('data_final')
  
  missoes = Missoes.query.filter(
    Missoes.data_lancamento >= datetime.strptime(data_inicial, '%Y-%m-%d'),
    Missoes.data_lancamento <= datetime.strptime(data_final, '%Y-%m-%d')
  ).order_by(Missoes.data_lancamento.desc()).all()
  
  return render_template('visualizar_missao.html', missoes=missoes)