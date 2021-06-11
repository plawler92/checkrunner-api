import os
import io
import yaml
import logging

import boto3

class S3YamlManager:
    def __init__(self, aws_access_key: str, aws_secret_access_key: str, 
        aws_role_arn: str, aws_external_id: str, s3_bucket: str, s3_folder: str):
        
        # self.sts_client = boto3.client(
        #     "sts",
        #     aws_access_key_id=aws_access_key,
        #     aws_secret_access_key=aws_secret_access_key
        # )
        self.access_key = aws_access_key
        self.secret_key = aws_secret_access_key
        self.role_arn = aws_role_arn
        self.external_id = aws_external_id
        self.s3_bucket = s3_bucket
        self.s3_folder = s3_folder
        # self.s3 = boto3.client("s3", aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_access_key)
        # self.s3_bucket = s3_bucket

    def get_files(self, s3_bucket=None) -> list[str]:
        bucket = s3_bucket if s3_bucket else self.get_s3_bucket()
        return [file.key for file in bucket.objects.filter(Prefix=self.s3_folder) if file.key[-1] != "/"]
        #return [key["Key"] for key in self.s3.list_objects(Bucket=self.s3_bucket)['Contents']]

    def get_yamls(self) -> list[dict]:
        bucket = self.get_s3_bucket()
        keys = self.get_files(bucket)
        yamls = []
        for key in keys:
            # data = self.s3.get_object(Bucket=self.s3_bucket, Key=key)
            # contents = data["Body"].read().decode("utf-8")
            contents = self.get_file_from_s3(key, bucket)
            yamls.append(yaml.load(contents, Loader=yaml.FullLoader))
        return yamls

    def get_file_from_s3(self, key, s3_bucket) -> str:
        bucket = s3_bucket if s3_bucket else self.get_s3_bucket()
        data = io.BytesIO()
        bucket.download_fileobj(key, data)
        return data.getvalue().decode("utf-8")


    def get_s3_bucket(self):
        creds = self._get_role_credentials()
        s3 = boto3.resource(
            "s3",
            aws_access_key_id=creds["AccessKeyId"],
            aws_secret_access_key=creds["SecretAccessKey"],
            aws_session_token=creds["SessionToken"]
        )

        return s3.Bucket(self.s3_bucket)


    def _get_role_credentials(self):
        sts_client = boto3.client(
            "sts",
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key
        )

        assumed_role_object = sts_client.assume_role(
            RoleArn=self.role_arn,
            RoleSessionName="Session2",
            ExternalId=self.external_id
        )

        return assumed_role_object["Credentials"]
