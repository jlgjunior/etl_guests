from app import dbStag as db

class Guest(db.Model):

  __tablename__ = 'guest'

  idHospede = db.Column(db.String(), primary_key=True)
  nome = db.Column(db.String(), nullable=False)
  email = db.Column(db.String(), nullable=False)
  dataNasc = db.Column(db.Date)
  dataHosped = db.Column(db.Date, nullable=False)

  def __init__(self, idHospede,nome,email,dataNasc,dataHosped):
    self.idHospede = idHospede
    self.nome = nome
    self.email = email
    self.dataNasc = dataNasc
    self.dataHosped = dataHosped
