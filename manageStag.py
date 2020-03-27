import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import appStag, dbStag
import configStag
from Guest import Guest

target_metadata = [dbStag.Model.metadata]

appStag.config.from_object(configStag.StagingConfigStag)

migrate = Migrate(appStag, dbStag)
manager = Manager(appStag)

@manager.command
def seed():
  dbStag.session.add_all([Guest('73F','Armando','armando@teste.com.br','01/03/1990','10/02/2017'),
  Guest('33W','João','joao@joao.com.br','21/01/1984','10/02/2017'), Guest('12D','José','jose@jose.com.br',None,'10/02/2017'),
  Guest('43F','Maico','maico@terra.com.br','22/11/1990','10/02/2017'),
  Guest('20S','Will','will@will.com.br','11/05/1950','10/02/2017'), Guest('84X','Carla','jose@jose.com.br','22/11/1991','10/02/2017')])
  dbStag.session.commit()

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()
