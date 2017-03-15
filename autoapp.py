from app.app import create_app
from app.setting import ProdConfig, DevConfig
from flask.helpers import get_debug_flag

config = DevConfig if get_debug_flag() else ProdConfig
app = create_app(config)

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
