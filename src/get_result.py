import json
import requests

def lambda_handler(event, context):
    try:
        request_id = event['pathParameters']['request_id']
        # Define the BFL API endpoint
        bfl_url = f'https://bflapi.com/get_result/{request_id}'
        # Make a GET request to the BFL API
        response = requests.get(bfl_url)
        # If the BFL request is successful
        if response.status_code == 200:
            data = response.json()
            
            # Return the response back to the client
            return {
                'statusCode': 200,
                'body': json.dumps(data)
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': 'Error retrieving generation result'})
            }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error'})
        }
