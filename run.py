import testrunner.file_util as futil

import config as cfg

if __name__ == "__main__":
    print(futil.get_files(cfg.tests_path))