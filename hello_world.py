import json

def lambda_handler(event, context):
    some_text = 'Hello World!'
    print(event, context)
    json_mylist = json.dumps(some_text, separators=(',', ':'))
    
    return {
        'statusCode': 200,
        'body': json_mylist
    } 
