from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class User(db.Model):
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), )