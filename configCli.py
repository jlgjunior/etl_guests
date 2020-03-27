import os

basedir = os.path.abspath(os.path.dirname(__file__))

class ConfigCli(object):
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  SECRET_KEY = 'application'
  SQLALCHEMY_DATABASE_URI = 'postgresql:///cli'

class ProductionConfigCli(ConfigCli):
  DEBUG = False

class StagingConfigCli(ConfigCli):
  DEVELOPMENT = True
  DEBUG = True

class DevelopmentConfigCli(ConfigCli):
  DEVELOPMENT = True
  DEBUG = True

class TestingConfigCli(ConfigCli):
  TESTING = True
