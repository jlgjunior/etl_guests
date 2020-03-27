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
  dbStag.session.add_all([Guest('73F','armando@teste.com.br','Armando','01/03/1990','10/02/2017'),
  Guest('33W','joao@joao.com.br','João','21/01/1984','10/02/2017'), Guest('12D','jose@jose.com.br','José',None,'10/02/2017'),
  Guest('43F','maico@terra.com.br','Maico','22/11/1990','10/02/2017'),
  Guest('20S','will@will.com.br','Will','11/05/1950','10/02/2017'), Guest('84X','jose@jose.com.br','Carla','22/11/1991','10/02/2017')])
  dbStag.session.commit()

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()
