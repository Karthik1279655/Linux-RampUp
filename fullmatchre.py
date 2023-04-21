#!/usr/bin/python3

import re
s = input('Enter pattern to check: ')
m = re.fullmatch(s, 'abcdefgh')
if m != None:
     print('Full string matched')
else:
     print('Full string not matched')




