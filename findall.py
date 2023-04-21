#!/usr/bin/python3

import re

text = "The cat in the hat sat on the mat."

pattern = r"\b\w{3}\b"
matches = re.findall(pattern, text)

print(matches)

