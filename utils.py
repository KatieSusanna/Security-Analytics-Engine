import re
import ipaddress
import random


def get_ip_address(line):
        ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if ip:
            return ip.group() 

def get_timestamp(line):
        timestamp = re.search(r"\d{2}/[a-zA-Z]{3}/\d{4}:\d{2}:\d{2}:\d{2}", line)
        if timestamp:
            return timestamp.group()

def get_status_code(line):
        status_code = re.search(r"\s\d{3}\s", line)
        if status_code:
            return status_code.group()


def get_path(line):
        path = re.search(r"http[s]?://[^\s]+", line)
        if path:
            return path.group(0)

def ip_generator(): 
      pass