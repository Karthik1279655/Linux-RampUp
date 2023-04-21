#!/usr/bin/python3

import re

pattern = r"\b\d{3}\b"
matches = []

with open('softwareTesting.txt', 'r') as file:
    for line in file:
        matches += re.findall(pattern, line)

print(matches)

