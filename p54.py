#!/usr/bin/env python

while True:
	year = int(raw_input('Enter a year, should be a 4 number integer:'))
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		print "Year %d is a LUNAR YEAR" %(year)
	else:
		print "Year %d is NOT a lunar Year" %(year)


