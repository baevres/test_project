import json

def lambda_handler(event, context):
    some_text = 'Hello World!'
    my_list = [some_text]
    json_mylist = json.dumps(my_list, separators=(',', ':'))
    
    return {
        'statusCode': 200,
        'body': json_mylist
    } 
