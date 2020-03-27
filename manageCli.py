import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import appCli, dbCli
import config
import Person

target_metadata = [dbCli.Model.metadata]

appCli.config.from_object(config.StagingConfigCli)

migrate = Migrate(appCli, dbCli)
manager = Manager(appCli)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()
