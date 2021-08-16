import requests
import json
import datetime


def circle():
    """
    Function take all records from MainTable - https://airtable.com/tbluOqbjxHEZoXg1r/viwKQMQcW0Baxtiim?blocks=hide
    with fields ID and title, sorted by ID.
    Circle take current record (Ex.: ID: 5, title: Проверка 3) and add it to mini_lst.
    When mini_lst have 3 records with current ID, ex.:
      ID - 5, Проверка 2
      ID - 5, Hello
      ID - 5, world
    The values of mini_lst will be added to main_lst and mini_lst clears.
    """
    key = 'key61gNeBIc9mp8RC' #my own api_key
    url = f'https://api.airtable.com/v0/appS74xV8aAeYBO5v/MainTable?fields%5B%5D=ID&fields%5B%5D=title&sort%5B0%5D%5Bfield%5D=ID&api_key={key}'
    main_lst = []
    req = requests.get(url).json()['records']
    l = len(req) - 1 # for iteration
    while True:
        for x in range(l + 1):
            if x <= l - 3:
                mini_lst = []
                for n in range(1, 4):
                    mini_lst.append(f"ID - {req[x]['fields']['ID']}, {req[x + n]['fields']['title']}")
                main_lst.append(mini_lst)

            elif (l - 3) < x < l:
                mini_lst = []
                rest = l - x
                dif = 3 - rest
                for n in range(1, rest+1):
                    mini_lst.append(f"ID - {req[x]['fields']['ID']}, {req[x + n]['fields']['title']}")

                for new_n in range(dif):
                    mini_lst.append(f"ID - {req[x]['fields']['ID']}, {req[new_n]['fields']['title']}")
                main_lst.append(mini_lst)

            elif x == l:
                mini_lst = []
                for n in range(3):
                    mini_lst.append(f"ID - {req[x]['fields']['ID']}, {req[n]['fields']['title']}")
                main_lst.append(mini_lst)
                break
        break

    return main_lst


def lambda_handler(event=None, context=None):
    lst = circle()
    lngth = len(lst) - 1
    now = int(datetime.datetime.now().strftime('%S'))
    while True:
        if now > lngth:
            now -= lngth
            continue
        break
    response = json.dumps(lst[now], ensure_ascii=False, separators=(',', ': '))
    return {
        'status': 200,
        'body': response
    }
