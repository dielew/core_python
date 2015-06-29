#!/usr/bin/env python

string1 = raw_input('please input a string:')
string2 = raw_input('please input another string:')

if string1[0] == string2[0] and (len(string1) == len(string2)):
	i = 1
	for i in range(len(string1)):
		if string1[i] != string2[i]:
			print 'unmatch'
			break
		elif i == len(string1) - 1:
			print 'match'	
else:
	print 'unmatch'
