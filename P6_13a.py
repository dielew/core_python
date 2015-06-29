#!/usr/bin/env python

import string

numlist_number = [ ]
digit_check = string.digits

numlist_string = raw_input('Please input a number string:')

if numlist_string in
	for i in numlist_string:
		numlist_number.append(int(i))
	numlist_number.sort()
	numlist_number_noninc = numlist_number[::-1]
	print numlist_number_noninc

else:
	print 'invalid string input, should all be digits!'
