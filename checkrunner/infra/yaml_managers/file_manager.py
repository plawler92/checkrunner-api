import os
import logging

from checkrunner.infra.yaml_managers.utils import convert_to_yaml

class FileManager:
    def __init__(self, checks_path):
        if os.path.exists(checks_path) is False or os.path.isdir(checks_path) is False:
            logging.warning(f"checks_path: {checks_path} doesn't exist or isn't a directory")
        self.checks_path = checks_path

    def get_files(self):
        try:
            return [
                os.path.join(self.checks_path, f)
                for f in os.listdir(self.checks_path)
                if os.path.isfile(os.path.join(self.checks_path, f)) and 
                os.path.splitext(f)[-1].lower() in [".yml", ".yaml"]
            ]
        except FileNotFoundError as e:
            logging.warning(str(e))
            return []

    def get_yamls(self):
        yamls = []
        files = self.get_files()
        for file in files:
            with open(file) as f:
                # yamls.append(yaml.load(f, Loader=yaml.FullLoader))
                yamls.extend(convert_to_yaml(f))
        return yamls

