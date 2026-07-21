from flask import Flask, request 
from datetime import datetime


app = Flask(__name__) 
LOG_FILE = 'logs.txt'

@app.after_request 
def log_request(response):
    ip = request.remote_addr
    timestamp = datetime.now().strftime('%d/%b/%Y:%H:%M:%S')
    method = request.method
    full_path = request.url
    status_code = response.status_code
    log_entry = f"{ip} - - [{timestamp}] \"{method} {full_path} HTTP/1.1\" {status_code} 512"
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry + "\n")

    return response 

@app.route("/login", methods=["POST"])


def login(): 
    username = request.form.get("username")
    password = request.form.get("password")


    correct_username = "admin"
    correct_password = "password123"

    return "Login successful" if username == correct_username and password == correct_password else "Login failed", 200 if username == correct_username and password == correct_password else 401

@app.route("/search", methods=["GET"]) 

def search():
    query = request.args.get("q")
    print(f"Received search query: {query}")
    return f"Search results for: {query}", 200

@app.route("/download", methods=["GET"])

def download():
    query = request.args.get("filename")
    print(f"Received download query: {query}")
    return f"Download results for: {query}", 200


if __name__ == "__main__":
        app.run (port=5000)

