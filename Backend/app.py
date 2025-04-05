from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, bcrypt, User

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@prontuario-db:5432/prontuario?sslmode=disable'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt.init_app(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email já cadastrado'}), 400

    user = User.criar_usuario(data['nome'], data['email'], data['senha'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Usuário registrado com sucesso'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and user.verificar_senha(data['senha']):
        return jsonify({'message': 'Login bem-sucedido'}), 200
    else:
        return jsonify({'message': 'Credenciais inválidas'}), 401

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
