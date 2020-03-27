import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import appStag, dbStag
import config
import Person

target_metadata = [dbStag.Model.metadata]

appStag.config.from_object(config.StagingConfigStag)

migrate = Migrate(appStag, dbStag)
manager = Manager(appStag)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()
