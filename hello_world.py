import json

def lambda_handler(event, context):
    some_text = 'Hello, World!'
    json_response = json.dumps(some_text, separators=(',', ':'))
    
    return {
        'statusCode': 200,
        'body': json_response
    } 
