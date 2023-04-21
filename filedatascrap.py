#!/usr/bin/python3

import re

pattern = '[0-9]{2}-[0-9]{2}-[0-9]{4}'

with open('softwareTesting.txt', 'r') as file:
    for data in file:
        date = re.findall(pattern, str(data))
        for n in date:
            print(n)

