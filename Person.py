from app import dbCli as db
from sqlalchemy import func

class Person(db.Model):

  __tablename__ = 'pessoas'

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(), nullable=False)
  email = db.Column(db.String(), nullable=False)
  idExterno = db.Column(db.String())
  dataCadastro = db.Column(db.Date, nullable=False)
  dataNasc = db.Column(db.Date)
  ultimaHosp = db.Column(db.Date)
  qtdeHospedag = db.Column(db.Integer)

  def __init__(self, id, nome, email, idExterno, dataCadastro, dataNasc, ultimaHosp, qtdeHospedag):
    if id is None:
      id = db.session.query(func.max(Person.id)).all()
    else:
      self.id = id
    self.nome = nome
    self.email = email
    self.idExterno = idExterno
    self.dataCadastro = dataCadastro
    self.dataNasc = dataNasc
    self.ultimaHosp = ultimaHosp
    self.qtdeHospedag = qtdeHospedag
