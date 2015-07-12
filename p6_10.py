#!/usr/bin/env python

import string
from p6_6 import blank_omit

str_list = list(raw_input('Enter a string with both uppercase and lowercase: '))
s =''

for i in range(len(str_list)):
	if str_list[i] in string.uppercase:
		str_list[i] = chr(ord(str_list[i]) + 32)
	elif str_list[i] in string.lowercase:
		str_list[i] = chr(ord(str_list[i]) - 32)
	else:
		pass
	s += str_list[i]
	
string_without_blank = blank_omit(s)
print string_without_blank



