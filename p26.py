#!/usr/bin/env python

while True:
	c = raw_input('PLZ input a number:')
	i = int(c)

	if i > 0:
		print 'positive number'

	elif i < 0:
		print 'negative mumber'

	else :
		print 'zero'
