import json

def lambda_handler(event, context):
    some_text = 'Hello Vasya!'
    json_mylist = json.dumps(some_text, separators=(',', ':'))
    
    return {
        'statusCode': 200,
        'body': json_mylist
    } 
