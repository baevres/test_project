import json
import time
import requests


def circle():
    """
    Function take all records from MainTable - https://airtable.com/tbluOqbjxHEZoXg1r/viwKQMQcW0Baxtiim?blocks=hide
    with fields ID and title, sorted by ID.
    Infinity circle take current record (Ex.: ID: 5, title: Проверка 3) and show next 3 records with current ID:
      ID - 5, Проверка 2
      ID - 5, Hello
      ID - 5, world
    When iteration reach limit (Ex.: ID: 14), circle begins again
    """
    key = 'key61gNeBIc9mp8RC' #my own api_key
    url = f'https://api.airtable.com/v0/appS74xV8aAeYBO5v/MainTable?fields%5B%5D=ID&fields%5B%5D=title&sort%5B0%5D%5Bfield%5D=ID&api_key={key}'
    main_lst = []
    req = requests.get(url).json()['records']
    l = len(req) - 1 # for iteration
    i = 0
    while i < 1:
        """
        The circle must had been infinity with iterations in 1 sec,
        but now 'lambda_handler' must`ve to response with interval in 1 sec
        """
        for x in range(l + 1):
            if x <= l - 3:
                mini_lst = []
                for n in range(1, 4):
                    mini_lst.append(f"ID - {req[x]['fields']['ID']}, {req[x + n]['fields']['title']}")
                main_lst.append(mini_lst)
                #time.sleep(1)


            elif (l - 3) < x < l:
                mini_lst = []
                rest = l - x
                dif = 3 - rest
                for n in range(1, rest+1):
                    mini_lst.append(f"ID - {req[x]['fields']['ID']}, {req[x + n]['fields']['title']}")

                for new_n in range(dif):
                    mini_lst.append(f"ID - {req[x]['fields']['ID']}, {req[new_n]['fields']['title']}")
                main_lst.append(mini_lst)

                #time.sleep(1)


            elif x == l:
                mini_lst = []
                for n in range(3):
                    mini_lst.append(f"ID - {req[x]['fields']['ID']}, {req[n]['fields']['title']}")
                main_lst.append(mini_lst)
                #time.sleep(1)

                i += 1
    return main_lst


def lambda_handler(event=None, context=None):
    text = circle()
    for x in text:
        print(x)
        yield {
            'status': 200,
            'body': x
        }
        time.sleep(1)
