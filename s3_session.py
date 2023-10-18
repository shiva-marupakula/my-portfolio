import boto3
import os


class Session():

    def create_session():
        session = boto3.Session(
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_KEY_ID']
        )
        s3_object=session.resource('s3')
        return s3_object