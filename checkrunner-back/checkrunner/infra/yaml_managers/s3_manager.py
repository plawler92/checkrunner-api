import os
import yaml
import logging

import boto3

class S3YamlManager:
    def __init__(self, aws_access_key: str, aws_secret_access_key: str, s3_bucket: str):
        self.s3 = boto3.client("s3", aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_access_key)
        self.s3_bucket = s3_bucket

    def get_files(self) -> list[str]:
        return [key["Key"] for key in self.s3.list_objects(Bucket=self.s3_bucket)['Contents']]

    def get_yamls(self) -> list[dict]:
        keys = self.get_files()
        yamls = []
        for key in keys:
            data = self.s3.get_object(Bucket=self.s3_bucket, Key=key)
            contents = data["Body"].read().decode("utf-8") # catch errors here?
            yamls.append(yaml.load(contents, Loader=yaml.FullLoader))
        return yamls