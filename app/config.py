

class Config:
    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI= "sqlite:///project.sqlite"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://flask:iti@localhost:5432/flask_py1"


project_config = {
    'dev': DevelopmentConfig,
    "prd": ProductionConfig
}


