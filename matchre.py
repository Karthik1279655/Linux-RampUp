#!/usr/bin/python3

import re
s = input('Enter pattern to check: ')
m = re.match(s, 'abcdefgh')
if m != None:
	print('Match is availale at the beginning of the string')
	print('Start Index: {} and End Index: {}'.format(m.start(), m.end()))
else:
	print('Match is not available at the beginning of the string')


