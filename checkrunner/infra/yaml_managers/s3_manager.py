"""
Exports a Class that reads yaml files from s3
"""
import io
import yaml

import boto3

from checkrunner.infra.yaml_managers.utils import convert_to_yaml, AWSS3Information

class S3YamlManager:
    """Gets yaml files from s3 and loads them into dicts"""
    def __init__(self, aws_details: AWSS3Information):
        self.aws_details = aws_details

    def get_yamls(self) -> list[dict]:
        """Returns a list of dictionaries read from yaml files in s3"""
        bucket = self.get_s3_bucket()
        keys = self.get_files(bucket)
        yamls = []
        for key in keys:
            contents = self.get_file_from_s3(key, bucket)
            #yamls.append(yaml.load(contents, Loader=yaml.FullLoader))
            yamls.extend(convert_to_yaml(contents))
        return yamls

    def get_files(self, s3_bucket=None) -> list[str]:
        """Returns a list of files in the given s3 bucket"""
        bucket = s3_bucket if s3_bucket else self.get_s3_bucket()
        return [
            file.key
            for file in bucket.objects.filter(Prefix=self.aws_details.s3_folder)
            if file.key[-1] != "/"
        ]

    def get_file_from_s3(self, key, s3_bucket) -> str:
        """Downloads the contents of a file in s3 by its key"""
        bucket = s3_bucket if s3_bucket else self.get_s3_bucket()
        data = io.BytesIO()
        bucket.download_fileobj(key, data)
        return data.getvalue().decode("utf-8")

    def get_s3_bucket(self):
        """Returns an boto s3 bucket object"""
        creds = self._get_role_credentials()
        s3_resource = boto3.resource(
            "s3",
            aws_access_key_id=creds["AccessKeyId"],
            aws_secret_access_key=creds["SecretAccessKey"],
            aws_session_token=creds["SessionToken"]
        )

        return s3_resource.Bucket(self.aws_details.s3_bucket)

    def _get_role_credentials(self):
        """Gets new credentials from aws"""
        sts_client = boto3.client(
            "sts",
            aws_access_key_id=self.aws_details.aws_access_key,
            aws_secret_access_key=self.aws_details.aws_secret_key
        )

        assumed_role_object = sts_client.assume_role(
            RoleArn=self.aws_details.aws_role_arn,
            RoleSessionName="Session2",
            ExternalId=self.aws_details.aws_external_id
        )

        return assumed_role_object["Credentials"]
