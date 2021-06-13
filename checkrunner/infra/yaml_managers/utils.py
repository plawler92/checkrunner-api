"""Utility functions for yaml managers"""
import yaml

def convert_to_yaml(file):
    """Loads all yaml documents in a file and returns them as a list"""
    return list(yaml.safe_load_all(file))
