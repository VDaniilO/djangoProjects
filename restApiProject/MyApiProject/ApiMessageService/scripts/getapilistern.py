import requests
import json

def get_message():
    url = "http://127.0.0.1:8000/api/v1/message/?format=json"
    data = requests.get(url).json()
    return data

result = get_message()
#print(result)

with open('result.json', 'w') as json_file:
    json.dump(result, json_file)
