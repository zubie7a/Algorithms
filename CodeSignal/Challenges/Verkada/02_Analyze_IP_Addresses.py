# https://app.codesignal.com/company-challenges/verkada/LgTPsbkr3hikeSNsD
from functools import reduce
import mysql.connector
import pandas as pd
import requests
import re
import os

# Otherwise the columns will be truncated with "..." even when reading them
# resulting in incomplete input when parsing the dataframes for IPs.
pd.set_option('display.max_colwidth', 1000)

files = []
# Navigate the root folder to get all files recursively because
# we don't know exactly how much files were created.
for root, directories, filenames in os.walk('/root'):
    for filename in filenames: 
        files.append(os.path.join(root,filename))

# A set to keep track of unique valid IPs.
valid_ips = set([])
# A function to validate IPs.
def validate_ip(ip):
    for octet in ip.split("."):
        value = int(octet)
        if value > 255:
            return False
    return True

# Read each file and then parse for IP-like values, to then
# validate each of those before adding to the set.
for filename in files:
    data = pd.read_csv(filename, delimiter="\n")
    string = data.to_string()
    matches = re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', string)
    for match in matches:
        if validate_ip(match):
            valid_ips.add(match)

for valid_ip in list(sorted(list(valid_ips))):
    print(valid_ip)
