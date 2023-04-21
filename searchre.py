#!/usr/bin/python3

import re
s = input('Enter pattern to check: ')
m = re.search(s, 'abaabaaab')
if m != None:
     print('Match is available')
     print('First occurrence with start index: {} and end index: {}'.format(m.start(), m.end()))
else:
     print('Not matched')





