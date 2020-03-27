from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from os import listdir
import os
from Person import Person
from Guest import Guest
from datetime import date

def main():
  for guest in Guest.query.all():
    person = Person(None, guest.nome, guest.email, guest.idHospede,date.today(),guest.dataNasc,guest.dataHosped,0)
    person.addNew() 

  #reader = DataReader('dataSrc')

  #data = reader.readCoordinates()
  
  #processor = DataProcessor(data)
  #models = processor.processDataPoints()
  #for model in models:
  #  try:
  #    db.session.add(model)
  #    db.session.commit()
  #  except Exception as e:
  #    db.session.rollback()
  #    print(e)


if __name__ == "__main__":
  main() 
