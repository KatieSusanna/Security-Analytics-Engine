import requests
from concurrent.futures import ThreadPoolExecutor

def run():
    url = "http://127.0.0.1:5000/login"

    wrong_passwords = ["12345", "letmein", "qwerty", "admin", "test123", "hunter2"]

    session = requests.Session()
    with ThreadPoolExecutor(max_workers=20) as executor:
        for pw in wrong_passwords: 
            data = {
                "username": "admin",
                "password": pw
            }

            # response = requests.post(url, data=data)
            executor.submit(session.post, url, data=data)


    final_data = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(url, data=final_data)
    print(response.status_code, response.text)

if __name__ == "__main__":
    run()