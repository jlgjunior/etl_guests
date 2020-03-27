from app import dbStag as db

class RawData(db.Model):

  __tablename__ = 'rawdata'

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(), nullable=False)
  email = db.Column(db.String(), nullable=False)
  dataHosped = db.Column(db.Date, nullable=False)

  def __init__(self,nome,email,dataHosped):
    self.nome = nome
    self.email = email
    print(dataHosped)
    hosped = dataHosped.split('-')
    self.dataHosped = hosped[2]+'-'+hosped[1]+'-'+hosped[0]

  def addNew(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
