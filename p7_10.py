#!/usr/bin/env python

import string

def rot13(string_ori):
	string_pro = ''
	for i in string_ori:
		if i in string.uppercase:
			asc_i = ord(i)
			if asc_i >= 65 and asc_i < 78:
				string_rotted = chr(asc_i + 13)
			else:
				string_rotted = chr(asc_i - 13)
		elif i in string.lowercase:
			asc_i = ord(i)
			if asc_i >= 97 and asc_i < 110:
				string_rotted = chr(asc_i + 13)
			else:
				string_rotted = chr(asc_i - 13)
		else:
			string_rotted = i
		string_pro += string_rotted
	return string_pro



if __name__ == '__main__':
	prompt = 'please enter a string:'
	origin_string = raw_input(prompt)
	print 'The encrypted string with rot13 rule is:  ', rot13(origin_string)



