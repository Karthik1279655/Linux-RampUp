#! /usr/bin/python3

import re

match = re.finditer('[abc]', 'a7b@k9z')
for m in match:
    print(m.start(), "th index of character: ", m.group())
print()

match1 = re.finditer('[^abc]', 'a7b@k9z')
for m in match1:
    print(m.start(), "th index of character: ", m.group())
print()

match2 = re.finditer('[a-z]', 'a7b@k9z')
for m in match2:
    print(m.start(), "th index of character: ", m.group())
print()

match3 = re.finditer('[A-Z]', 'a7b@k9z')
for m in match3:
    print(m.start(), "th index of character: ", m.group())
print()

match4 = re.finditer('[0-9]', 'a7b@k9z')
for m in match4:
    print(m.start(), "th index of character: ", m.group())
print()

