#!/usr/bin/env python

while True:
	money = int(raw_input('Please enter the total number of coins for change(<100 and >0):'))
	if (money < 100 and money > 0):
		c25 = money // 25
		r25 = money % 25
		c10 = r25 // 10
		r10 = r25 % 10
		c5  = r10 // 5
		r5  = r10 % 5
		c1  = r5 // 1
		print 'various coins for change are:\ncoin 25cents: %d\ncoin 10cents: %d\ncoin 5cents: %d\ncoin 1cent: %d' %(c25, c10, c5, c1)
	else:
		print 'sorry, invalid input range, should less than 100 cents and more than 0 cents:'

 		
