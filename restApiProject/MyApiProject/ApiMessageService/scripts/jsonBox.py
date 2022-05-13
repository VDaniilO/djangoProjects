import json
import requests


EXCEPT = 'АБРАКАДАБРА'

url = "http://127.0.0.1:8000/api/v1/message/?format=json"
myToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyNDI4ODYxLCJqdGkiOiI4ZTk2MzI1YmU4NDM0ODQwYTgxYzkxMGRhMzliOGM3MCIsInVzZXJfaWQiOjF9.NPsHt2PtN0u9xw_lXd3jef_kQdeaImAkGnJiEFq55wU'
head = {'Authorization': 'JWToken {}'.format(myToken)}

def get_message():
    data = requests.get(url).json()
    return data

result = get_message()

def put_req(id_usr = None, name_usr = None, ver = True):

    if EXCEPT.lower() in message_text:
        requests.put(f'http://127.0.0.1:8000/api/v1/message/{id_usr}/', headers = head,  data = {'nameUsr': name_usr, 'verify': ver, 'condition': 2})
    elif EXCEPT in message_text:
        requests.put(f'http://127.0.0.1:8000/api/v1/message/{id_usr}/', headers = head,  data = {'nameUsr': name_usr, 'verify': ver, 'condition': 2})
    else:
        requests.put(f'http://127.0.0.1:8000/api/v1/message/{id_usr}/', headers = head,  data = {'nameUsr': name_usr, 'verify': ver, 'condition': 3})


while result:
    for all_data in result['results']:
        id_usr = all_data['id']
        name_usr = all_data['nameUsr']
        message_text = all_data['message']
        verify_value = all_data['verify']
        condition_value = all_data['condition']

        put_req(id_usr, name_usr)
