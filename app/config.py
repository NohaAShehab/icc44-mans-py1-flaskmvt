

class Config:
    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG=1
    SQLALCHEMY_DATABASE_URI= "sqlite:///project.sqlite"


class ProductionConfig(Config):
    DEBUG = 0
    SQLALCHEMY_DATABASE_URI = "postgresql://flask:iti@localhost:5432/flask_py1"


config = {
    'dev': DevelopmentConfig,
    "prd": ProductionConfig
}


