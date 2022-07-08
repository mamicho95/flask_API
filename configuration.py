class BaseConfig(object):
    'Base configuracion'
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False
class ProductionConfig(BaseConfig):
    'Produccion configuracion'
    DEBUG = False
class DevelopmentConfig(BaseConfig):
    'Desarrollo configuracion'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/apialmacen"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Desarrollo key'