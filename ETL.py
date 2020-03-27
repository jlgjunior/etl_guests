import os
from os import listdir
from Person import Person
from Guest import Guest
from datetime import date
from RawData import RawData
from threading import Timer

def main():
  importData()
  
  while True:
    continue

def importData():
  importFromGuest()
  readRawDataFromFile()
  importFromRawData()
  timer = Timer(30.0, importData)
  timer.start()

def readRawDataFromFile():
  for fileName in listdir('data'):
    fullname = os.path.join('data', fileName)
    lines = open(fullname).readlines()
    for i in range(1, len(lines)):
      line = lines[i]
      items = line.strip().split('\t')
      rawData = RawData(items[1], items[0], items[2])
      rawData.addNew()
    os.rename(fullname, os.path.join('doneFiles', fileName))

def importFromRawData():
  for rawData in RawData.query.all():
    person = Person.createFromRawData(rawData)
    rawData.delete()
    person.addNew() 

def importFromGuest():
  for guest in Guest.query.all():
    person = Person(None, guest.nome, guest.email, guest.idHospede,date.today(),guest.dataNasc,guest.dataHosped,0)
    person.addNew() 



if __name__ == "__main__":
  main() 
