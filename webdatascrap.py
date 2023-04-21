#!/usr/bin/python3

import re
import json

with open('output.json') as f:
    try:
        data = json.load(f)
    except json.JSONDecodeError:
        print('Error: Invalid JSON data in file')
        exit()

pincodes = re.findall(r'\b\d{6}\b', str(data))
for pincode in pincodes:
    print(pincode)


