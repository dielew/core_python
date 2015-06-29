#!/usr/bin/env python

a = [x * 0 for x in range(5)]

for i in range(5):
	a[i] = float(raw_input('please enter a number:'))

print (sum(a)/5.0)


