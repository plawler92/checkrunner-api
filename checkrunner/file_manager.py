import os
import yaml

class FileManager:
    def __init__(self, checks_path):
        self.checks_path = checks_path

    def get_files(self):
        return [
            os.path.join(self.checks_path, f)
            for f in os.listdir(self.checks_path)
            if os.path.isfile(os.path.join(self.checks_path, f)) and 
            os.path.splitext(f)[-1].lower() in [".yml", ".yaml"]
        ]

    def get_yamls(self):
        yamls = []
        files = self.get_files()
        for file in files:
            with open(file) as f:
                yamls.append(yaml.load(f, Loader=yaml.FullLoader))
        return yamls

