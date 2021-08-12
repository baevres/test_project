import json

import requests


def circle(event=None, context=None):
    """
    Function take all records from MainTable - https://airtable.com/tbluOqbjxHEZoXg1r/viwKQMQcW0Baxtiim?blocks=hide
    with fields ID and title, sorted by ID.
    Infinity circle take current record (Ex.: ID: 5, title: Проверка 3) and show next 3 records with current ID:
      ID - 5, Проверка 2
      ID - 5, Hello
      ID - 5, world
    When iteration reach limit (Ex.: ID: 14), circle begins again
    """
    import time
    key = 'key61gNeBIc9mp8RC' #my own api_key
    url = f'https://api.airtable.com/v0/appS74xV8aAeYBO5v/MainTable?fields%5B%5D=ID&fields%5B%5D=title&sort%5B0%5D%5Bfield%5D=ID&api_key={key}'

    req = requests.get(url).json()['records']
    l = len(req) - 1 # for iteration

    while True:
        """
        circle will be infinity, but every iteration have interval in 1 sec
        """
        for x in range(l + 1):
            if x <= l - 3:
                for n in range(1, 4):
                    print(f"ID - {req[x]['fields']['ID']},", req[x + n]['fields']['title'])

                time.sleep(1)
                print()

            elif (l - 3) < x < l:
                rest = l - x
                dif = 3 - rest
                for n in range(1, rest+1):
                    print(f"ID - {req[x]['fields']['ID']},", req[x + n]['fields']['title'])

                for new_n in range(dif):
                    print(f"ID - {req[x]['fields']['ID']},", req[new_n]['fields']['title'])
                time.sleep(1)
                print()

            elif x == l:
                for n in range(3):
                    print(f"ID - {req[x]['fields']['ID']},", req[n]['fields']['title'])
                time.sleep(1)
                print()


circle()

# def lambda_handler(event, context):
#     some_text = 'Hello, World!'
#     json_response = json.dumps(some_text, separators=(',', ':'))
    
#     return {
#         'statusCode': 200,
#         'body': json_response
#     } 
