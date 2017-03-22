class Config:
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    ENDPOINT = "http://localhost:5000/"
    pass
