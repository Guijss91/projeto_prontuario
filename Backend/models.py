from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)

    def verificar_senha(self, senha_plaintext):
        return bcrypt.check_password_hash(self.senha_hash, senha_plaintext)

    @staticmethod
    def criar_usuario(nome, email, senha):
        senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')
        return User(nome=nome, email=email, senha_hash=senha_hash)
