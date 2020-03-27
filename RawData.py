from app import dbStag as db

class RawData(db.Model):

  __tablename__ = 'rawdata'

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(), nullable=False)
  email = db.Column(db.String(), nullable=False)
  dataHosped = db.Column(db.Date, nullable=False)

  def __init__(self, id,nome,email,dataHosped):
    self.nome = nome
    self.email = email
    self.dataHosped = dataHosped
