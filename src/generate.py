import json
import requests  # Use the requests library to make HTTP calls

def lambda_handler(event, context):
    try:
        # Parse the input body from the event
        body = json.loads(event['body'])
        
        # Define the BFL API endpoint
        bfl_url = 'https://bflapi.com/generate'
        
        # Make a POST request to the BFL API
        response = requests.post(bfl_url, json=body)
        
        # If the BFL request is successful
        if response.status_code == 200:
            data = response.json()
            
            # Prepare the response format
            result = {
                'request_id': data.get('request_id'),
                'status': data.get('status', 'processing'),  # Default to 'processing' if not found
                'result': {
                    'text': data.get('text', ''),
                    'metadata': {
                        'tokens_used': data.get('tokens_used', 0),
                        'processing_time': data.get('processing_time', 0)
                    }
                }
            }
            
            return {
                'statusCode': 200,
                'body': json.dumps(result)
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': 'Error initiating generation request'})
            }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error'})
        }
