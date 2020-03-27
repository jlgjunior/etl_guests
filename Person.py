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
    self.id = id
    self.nome = nome
    self.email = email
    self.idExterno = idExterno
    self.dataCadastro = dataCadastro
    self.dataNasc = dataNasc
    self.ultimaHosp = ultimaHosp
    self.qtdeHospedag = qtdeHospedag

  def addNew(self):
    listPeople = db.session.query(Person).filter(Person.idExterno == self.idExterno).all() 
    if listPeople == []:
      print('adding')
      self.id = db.session.query(func.max(Person.id)).all()[0][0]+1
      db.session.add(self)
      db.session.commit()
    else:
      oldPerson = listPeople[0]
      self.id = oldPerson.id
      if oldPerson.qtdeHospedag is None:
        oldPerson.qtdeHospedag = 0
      if oldPerson.ultimaHosp != self.ultimaHosp:
        self.qtdeHospedag = oldPerson.qtdeHospedag + 1
      db.session.merge(self)
      db.session.commit()
      print('already exists')

