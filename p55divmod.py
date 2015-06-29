#!/usr/bin/env python

while True:
	money = int(raw_input('Please enter a number:'))
	if money > 0 and money < 100:
		(c25, r25) = divmod(money, 25)
		(c10, r10) = divmod(r25, 10)
		(c5,  r5)  = divmod(r10, 5)
		(c1,  r1)  = divmod(r5, 1)
		print 'coins for %d cents are:\n\ncoin 25cents:%d\ncoin 10cents:%d\ncoin 5cents:%d\ncoin 1cent:%d'\
				%(money, c25,c10, c5, c1)
	else:
		print 'invalid input range, should be a integer < 100 and > 0:'
