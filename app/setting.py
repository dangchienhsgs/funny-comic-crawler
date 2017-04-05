class Config:
    ENDPOINT = "https://funny-comic-server.herokuapp.com"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    ENDPOINT = "http://localhost:5000"
    SQLALCHEMY_DATABASE_URI = 'postgresql://dangchienhsgs:123456@localhost:5432/funny_comic'
