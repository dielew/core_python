#!/usr/bin/env python

num_list_ord = [ ] 
num_list_lexisort_noninc = [ ]

num_string = raw_input('Please enter a string of numbers:')

for i in num_string:
	num_list_ord.append(ord(i))

num_list_ord.sort()
num_list_ord_noninc = num_list_ord[::-1]

for i in num_list_ord_noninc:
	num_list_lexisort_noninc.append(int(chr(i)))

print num_list_lexisort_noninc





