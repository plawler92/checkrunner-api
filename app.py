import logging
#from logging.config import dictConfig

#from checkrunner import create_app
from checkrunner.api import create_app
from config import Config

cfg = Config()

logging.basicConfig(
    level=cfg.LOG_LEVEL,
    format="%(asctime)s - %(filename)s - %(funcName)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# dictConfig(cfg.LoggerConfig.LOGGING_CONFIG)

app = create_app(cfg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)