import requests

url = "http://127.0.0.1:5000/login"

wrong_passwords = ["12345", "letmein", "qwerty", "admin", "test123", "hunter2"]

for pw in wrong_passwords: 
    data = {
        "username": "admin",
        "password": pw
    }

    response = requests.post(url, data=data)
    print(response.status_code, response.text)

final_data = {
    "username": "admin",
    "password": "password123"
}

response = requests.post(url, data=final_data)
print(response.status_code, response.text)