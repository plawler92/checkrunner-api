"""Utility functions for yaml managers"""
from dataclasses import dataclass

import yaml

def convert_to_yaml(file):
    """Loads all yaml documents in a file and returns them as a list"""
    return list(yaml.safe_load_all(file))

@dataclass
class AWSS3Information:
    """Data class to store aws credentials"""
    aws_access_key: str
    aws_secret_key: str
    aws_role_arn: str
    aws_external_id: str
    s3_bucket: str
    s3_folder: str
