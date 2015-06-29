#!/usr/bin/env python


a = [x * 0 for x in range(5)]
for i in range(5):
	a[i] = int(raw_input('Please enter a number:'))

print sum(a)
