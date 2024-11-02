from app import app
from flask import request, Blueprint, jsonify
from app.modelos.database import db
from app.modelos.models import Missoes
from datetime import datetime

bp = Blueprint('missao', __name__)

@app.route('/')
def index():
    return jsonify({'message': 'Bem vindo ao sistema de gerenciamento espacial!'}), 200

@app.route('/missao/adicionar', methods=['GET', 'POST'])
def adicionar_missao():
  try:
    data = request.get_json()
  
    required_fields = ['nome_missao', 'data_lancamento', 'destino', 'estado_missao', 'tripulacao', 'carga_util', 'duracao_missao', 'custo_missao', 'status_missao']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
      return jsonify({'error': f'Campos Obrigatórios ausentes: {", ".join(missing_fields)}'}), 400
    
    nova_missao = Missoes(
      nome_missao=data['nome_missao'],
      data_lancamento=datetime.strptime(data['data_lancamento'], '%Y-%m-%d'),
      destino=data['destino'],
      estado_missao=data['estado_missao'],
      tripulacao=data['tripulacao'],
      carga_util=data['carga_util'],
      duracao_missao=data['duracao_missao'],
      custo_missao=data['custo_missao'],
      status_missao=data['status_missao']
    )
    db.session.add(nova_missao)
    db.session.commit()
    return jsonify({'message':'Missão adicionada com sucesso!', 'missao': nova_missao.to_dict()}), 201
  except Exception as e:
      return jsonify({"error": str(e)}), 500

@app.route('/missao/editar/<int:id>', methods=['GET', 'PUT'])
def editar_missao(id):
  try:
    missao = Missoes.query.get_or_404(id)
    
    if request.method == 'PUT':  
      data = request.get_json()
      
      required_fields = ['nome_missao', 'data_lancamento', 'destino', 'estado_missao', 'tripulacao', 'carga_util', 'duracao_missao', 'custo_missao', 'status_missao']
      missing_fields = [field for field in required_fields if field not in data]
      
      if missing_fields:
        return jsonify({'error': f'Campos Obrigatórios ausentes: {", ".join(missing_fields)}'}), 400
      
      missao.nome_missao=data['nome_missao']
      missao.data_lancamento=datetime.strptime(data['data_lancamento'], '%Y-%m-%d')
      missao.destino=data['destino']
      missao.estado_missao=data['estado_missao']
      missao.tripulacao=data['tripulacao']
      missao.carga_util=data['carga_util']
      missao.duracao_missao=data['duracao_missao']
      missao.custo_missao=data['custo_missao']
      missao.status_missao=data['status_missao']
      
      db.session.commit()
      return jsonify({'message': 'Missão atualizada com sucesso!', 'missao': missao.to_dict()}), 200
      
    return jsonify(missao.to_dict()), 200
  except Exception as e:
      return jsonify({"error": str(e)}), 500
    
@app.route('/missao/deletar/<int:id>', methods=['DELETE'])
def deletar_missao(id):
  try:
    missao = Missoes.query.get_or_404(id)

    db.session.delete(missao)
    db.session.commit()
    
    return jsonify({'message': 'Missao deletada com sucesso!'}), 200
  except Exception as e:
      return jsonify({"error": str(e)}), 500
    
@app.route('/missao', methods=['GET'])
def visualizar_missao():
  try:
    missoes = Missoes.query.order_by(Missoes.data_lancamento.desc()).all()
    return jsonify([missao.to_dict() for missao in missoes])
  except Exception as e:
    return jsonify({"error": str(e)}), 500

@app.route('/missao/<int:id>', methods=['GET'])
def detalhes_missao(id):
    missao = Missoes.query.get_or_404(id)
    return jsonify(missao.to_dict()), 200

@app.route('/missao/pesquisar', methods=['GET'])
def pesquisar_missao():
  try:
    data_inicial = request.args.get('data_inicial')
    data_final = request.args.get('data_final')
    
    if not data_final or not data_inicial:
      return jsonify({'error': 'As datas inicial e final são obrigatórias!'}), 400
    
    try:
      data_inicial = datetime.strptime(data_inicial, '%Y-%m-%d')
      data_final = datetime.strptime(data_final, '%Y-%m-%d')
    except:
      return jsonify({'error': 'O formato das datas deve ser YYYY-MM-DD.'}), 400
    
    missoes = Missoes.query.filter(
      Missoes.data_lancamento >= data_inicial,
      Missoes.data_lancamento <= data_final
    ).order_by(Missoes.data_lancamento.desc()).all()
    
    return jsonify([missao.to_dict() for missao in missoes]), 200
  except Exception as e:
      return jsonify({"error": str(e)}), 500