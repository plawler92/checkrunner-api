# import testrunner.file_util as futil

# import config as cfg

# if __name__ == "__main__":
#     print(futil.get_files(cfg.tests_path))

from checkrunner import create_app
from config import Config

app = create_app(Config())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)