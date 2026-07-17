import re

class ddos_check:
    def __init__(self, logs):
        self.log_lines = logs
        self.ip_timestamps = {}

    def check_ddos(self):
        ddos = False
        for line in self.log_lines:
            ip_address = self.get_ip_address(line)
            timestamp = self.get_timestamp(line)

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
            

    def get_ip_address(self, line):
        ip = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if ip:
            return ip.group() 

    def get_timestamp(self, line):
        timestamp = re.search("\d{2}/[a-zA-Z]{3}/\d{4}:\d{2}:\d{2}:\d{2}", line)
        if timestamp:
            return timestamp.group()
        
class brute_force_check:
    def __init__ (self, logs):
        self.log_lines = logs
        self.ip_attempts = {}

    def check_brute_force(self):
        line = self.log_lines[0]
        print(line)

    
    def get_ip_address(self, line):
        ip = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if ip:
            return ip.group() 
        
    def get_outcome(self, line):
        pass



    



def main(): 
    rawLogs = open("logs.txt", "r")
    logs = rawLogs.readlines()
    ddos_checker = ddos_check(logs)
    ddos_checker.check_ddos()
    brute_force_checker = brute_force_check(logs)
    brute_force_checker.check_brute_force()
    rawLogs.close()

main() 