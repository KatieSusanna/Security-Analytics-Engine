import requests

url = "http://127.0.0.1:5000/login"
session = requests.Session()

for i in range(150):
    response = session.post(url)

