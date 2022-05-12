import json
import requests


EXCEPT = 'АБРАКАДАБРА'
myToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMzg1Njg5LCJqdGkiOiI4Y2JhZWNkMWEyYzI0YzBhODYwMGMwNTgyMWEyNDFiYSIsInVzZXJfaWQiOjF9.UX2dUNyKY7wAf8BrxfKSzYLdD_fgzZcBAWDSsFwQIMo'
head = {'Authorization': 'JWToken {}'.format(myToken)}

def get_message():
    url = "http://127.0.0.1:8000/api/v1/message/?format=json"
    data = requests.get(url).json()
    return data

result = get_message()


for all_data in result['results']:
    id_usr = all_data['id']
    name_usr = all_data['nameUsr']
    message_text = all_data['message']
    verify_value = all_data['verify']
    condition_value = all_data['condition']

    if EXCEPT.lower() in message_text:
        requests.put(f'http://127.0.0.1:8000/api/v1/message/{id_usr}/', headers = head,  data = {'nameUsr': name_usr, 'verify': True, 'condition': 2})

    elif EXCEPT in message_text:
        requests.put(f'http://127.0.0.1:8000/api/v1/message/{id_usr}/', headers = head,  data = {'nameUsr': name_usr, 'verify': True, 'condition': 2})

    else:
        requests.put(f'http://127.0.0.1:8000/api/v1/message/{id_usr}/', headers = head,  data = {'nameUsr': name_usr, 'verify': True, 'condition': 3})
