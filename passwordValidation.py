#!/usr/bin/python3

import re

valid_passwords = []

passwords = input("Enter the passwords (separated by commas): ").split(',')

for password in passwords:

    if (7 <= len(password) <= 12) and re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password) and re.search("[#$@]", password):
        valid_passwords.append(password)

print("Valid passwords:", ", ".join(valid_passwords))



