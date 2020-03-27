from app import dbCli as db
from sqlalchemy import func
from RawData import RawData
from datetime import date, datetime

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
  dataAtualizacao = db.Column(db.DateTime)

  def __init__(self, id, nome, email, idExterno, dataCadastro, dataNasc, ultimaHosp, qtdeHospedag, dataAtualizacao):
    self.id = id
    self.nome = nome
    self.email = email
    self.idExterno = idExterno
    self.dataCadastro = dataCadastro
    self.dataNasc = dataNasc
    self.ultimaHosp = ultimaHosp
    self.qtdeHospedag = qtdeHospedag
    self.dataAtualizacao = dataAtualizacao

  @classmethod
  def createFromRawData(cls,rawData):
    return Person(None,rawData.nome,rawData.email,None,date.today(),None,rawData.dataHosped,1,None)

  def addNew(self):
    listPeople = db.session.query(Person).filter(Person.idExterno == self.idExterno, Person.idExterno != None).all()
    self.dataAtualizacao = datetime.now()
    if listPeople == []:
      self.id = db.session.query(func.max(Person.id)).all()[0][0]+1
      if (not self.ultimaHosp is None) and (self.qtdeHospedag is None):
        self.qtdeHospedag = 1
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
