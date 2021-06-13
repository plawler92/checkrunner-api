import yaml

def convert_to_yaml(file):
     return [y for y in yaml.safe_load_all(file)]
        