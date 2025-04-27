import boto3

client = boto3.client('cognito-idp')

USER_POOL_ID = os.environ['USER_POOL_ID']

def handler(event, context):
    email = event['email']
    password = event['password']

    response = client.sign_up(
        ClientId=os.environ['COGNITO_CLIENT_ID'],
        Username=email,
        Password=password,
        UserAttributes=[
            {'Name': 'email', 'Value': email},
        ],
    )

    return {
        'statusCode': 200,
        'body': 'User signup successful! Please verify your email.'
    }
