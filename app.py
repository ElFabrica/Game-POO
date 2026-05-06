"""
=============================================================
  MODULE: app.py
  Servidor Flask para executar o jogo via landing page
=============================================================
"""

import os
import sys
import subprocess
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from pathlib import Path

# Garante que o diretório do projeto está no path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Define o diretório base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=BASE_DIR)
CORS(app)  # Permite requisições de qualquer origem

# Gera imagens se ainda não existem
from generate_assets import generate_all
from config import ASSETS_DIR

if not os.path.exists(os.path.join(ASSETS_DIR, "card_back.png")):
    print("Gerando assets das linguagens...")
    generate_all()


@app.route('/')
def index():
    """Serve a landing page"""
    return send_from_directory(BASE_DIR, 'index.html')


@app.route('/api/play', methods=['POST'])
def play_game():
    """Inicia a aplicação do jogo"""
    try:
        # Caminho do arquivo main.py
        main_file = os.path.join(os.path.dirname(__file__), 'main.py')
        
        # Executa o jogo em um processo separado
        subprocess.Popen([sys.executable, main_file])
        
        return jsonify({
            'success': True,
            'message': 'Jogo iniciado! Verifique a janela do Pygame.'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Erro ao iniciar o jogo: {str(e)}'
        }), 500


if __name__ == '__main__':
    print("=" * 60)
    print("  CodeMemory — Servidor iniciado")
    print("=" * 60)
    print("  🌐 Acesse: http://localhost:5000")
    print("  ⚠️  Certifique-se que pygame está instalado")
    print("=" * 60)
    app.run(debug=True, port=5000)
