import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import appCli, dbCli
import configCli
from Person import Person
from datetime import datetime

target_metadata = [dbCli.Model.metadata]

appCli.config.from_object(configCli.StagingConfigCli)

migrate = Migrate(appCli, dbCli)
manager = Manager(appCli)

@manager.command
def seed():
  dbCli.session.add_all([Person(123,'João','joao@joao.com.br','22E','01/02/2017',None,'22/10/2010',1,datetime.now()),
  Person(456,'Maria','maria@maria.com.br',None,'01/02/2015',None,None,None,datetime.now()),
  Person(789,'José','jose@jose.com.br','12D','04/01/2016',None,'01/01/2015',3,datetime.now()),
  Person(990,'Maico','maico@terra.com.br','43F','01/02/2015',None,'09/10/2009',10,datetime.now())])
  dbCli.session.commit()
  

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()
