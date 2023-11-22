import json
import boto3
# import requests

def create_bucket(bucket_name:str , region=None ):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                        CreateBucketConfiguration=location)
    except:
        return {
        "statusCode": 500,
        "body": json.dumps({
            "message": "General Error",
        }),
    }
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Success",
        }),
    }

def lambda_handler(event, context):
    create_bucket("teste_carga", "us-east-1")
