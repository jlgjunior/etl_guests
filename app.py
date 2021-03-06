from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import configCli, configStag

appStag = Flask(__name__)
appStag.config.from_object(configStag.StagingConfigStag)
appStag.config['SQL_ALCHEMY_TRACK_MODIFICATIONS'] = False

appCli = Flask(__name__)
appCli.config.from_object(configCli.StagingConfigCli)
appCli.config['SQL_ALCHEMY_TRACK_MODIFICATIONS'] = False

dbStag = SQLAlchemy(appStag)
dbCli = SQLAlchemy(appCli)

if __name__ == '__main__':
  appCli.run()
  appStag.run()
