import os

basedir = os.path.abspath(os.path.dirname(__file__))

class ConfigStag(object):
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  SECRET_KEY = 'application'
  SQLALCHEMY_DATABASE_URI = 'postgresql:///stag_int'

class ProductionConfigStag(ConfigStag):
  DEBUG = False

class StagingConfigStag(ConfigStag):
  DEVELOPMENT = True
  DEBUG = True

class DevelopmentConfigStag(ConfigStag):
  DEVELOPMENT = True
  DEBUG = True

class TestingConfigStag(ConfigStag):
  TESTING = True
