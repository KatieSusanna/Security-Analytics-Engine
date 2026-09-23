import re
from utils import get_ip_address, get_timestamp, get_status_code, get_path 

class ddos_check:
    def __init__(self, logs):
        self.log_lines = logs
        self.ip_timestamps = {}

    def check_ddos(self):
        ddos = False
        for line in self.log_lines:
            ip_address = get_ip_address(line)
            timestamp = get_timestamp(line)

            ip_timestamp = (ip_address, timestamp)

            if ip_timestamp in self.ip_timestamps:
                self.ip_timestamps[ip_timestamp] += 1
            else:  
                self.ip_timestamps[ip_timestamp] = 1

            
        for log in self.ip_timestamps:
            if self.ip_timestamps[log] > 100:
                print(f"Potential DDoS attack detected from IP: {log[0]} at {log[1]} with {self.ip_timestamps[log]} requests.")
                ddos = True

        if not ddos:
            print("No DDoS attack detected.")



class brute_force_check:
    def __init__ (self, logs):
        self.log_lines = logs
        self.ip_attempts = {}

    def check_brute_force(self):

        

        for line in self.log_lines:
            ip_address = get_ip_address(line)
            status_code = get_status_code(line)


            if ip_address in self.ip_attempts:
                if status_code == " 401 ":
                    self.ip_attempts[ip_address] += 1
                if status_code == " 404 ":
                    self.ip_attempts[ip_address] += 1
                elif status_code == " 200 ":
                    attempt_count = self.ip_attempts[ip_address]
                    if attempt_count > 5:
                        print(f"Potential brute force attack detected from IP: {ip_address} with {attempt_count} failed attempts.")
            elif status_code == " 401 ":
                self.ip_attempts[ip_address] = 1
            elif status_code == " 404 ":
                self.ip_attempts[ip_address] = 1




class sqli_check: 
    def __init__ (self, logs):
        self.log_lines = logs
        self.sus_words = ["DROP", "TABLE", "SELECT", "INSERT", "DELETE", "UPDATE", "WHERE", "OR", "AND", "--", ";", "admin", "1=1", "LIMIT", "ORDER BY"]

    def check_sqli(self):
        sqli = False
        for line in self.log_lines:
            path =get_path(line)
            if path:
                for word in self.sus_words:
                    if word in path:
                        print(f"Potential SQL Injection attempt detected in request: {line.strip()}")
                        sqli = True
                        break

    
    

class traversal_check:
    
    def __init__(self, logs):
        self.log_lines = logs
        self.traversal_patterns = ["../", "..\\", "%2e%2e%2f", "%2e%2e\\", "..%2f", "..%5c"]

    def check_traversal(self):
        traversal = False
        for line in self.log_lines:
            path = self.get_path(line)
            if path:
                for pattern in self.traversal_patterns:
                    if pattern in path:
                        print(f"Potential Path Traversal attempt detected in request: {line.strip()}")
                        traversal = True
                        break

    def get_path(self, line):
        path = re.search(r"http[s]?://[^\s]+", line)
        if path:
            return path.group(0)

def main(): 
    rawLogs = open("logs.txt", "r")
    logs = rawLogs.readlines()
    ddos_checker = ddos_check(logs)
    ddos_checker.check_ddos()
    brute_force_checker = brute_force_check(logs)
    brute_force_checker.check_brute_force()
    sqli_checker = sqli_check(logs)
    sqli_checker.check_sqli()
    traversal_checker = traversal_check(logs)
    traversal_checker.check_traversal()
    rawLogs.close()

main() 