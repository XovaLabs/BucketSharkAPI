import requests
import json

payload = {
  "name": "Carlos",
  "description": "Carlos is crazy LOL"
}
response = requests.post('https://localhost:7144/Category', verify=False, json=payload)
print(response.text)