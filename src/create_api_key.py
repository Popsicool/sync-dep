import boto3
import os

apigateway = boto3.client('apigateway')

def handler(event, context):
    user_id = event['user_id']
    response = apigateway.create_api_key(
        name=f"{user_id}-apikey",
        enabled=True,
        generateDistinctId=True
    )

    api_key_id = response['id']
    api_key_value = response['value']

    return {
        'statusCode': 200,
        'body': {
            'apiKeyId': api_key_id,
            'apiKey': api_key_value
        }
    }
