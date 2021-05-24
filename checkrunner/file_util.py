import os
import yaml

def get_files(path):
    return [
        os.path.join(path, f)
        for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f)) and
        os.path.splitext(f)[-1].lower() in [".yml", ".yaml"]
    ]

def read_yaml(file):
    with open(file) as f:
        y = yaml.load(f, Loader=yaml.FullLoader)
        return y
