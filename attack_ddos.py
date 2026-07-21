import requests
from concurrent.futures import ThreadPoolExecutor

def run():
    url = "http://127.0.0.1:5000/login"

    # for i in range(150):
    #     response = requests.post(url)
        
    session = requests.Session() 
    with ThreadPoolExecutor(max_workers=20) as executor:
        for i in range(150):
            executor.submit(session.post, url)

if __name__ == "__main__":
    run()