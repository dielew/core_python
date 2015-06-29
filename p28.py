#!/usr/bin/env python

i = 0
s = [x * 0 for x in range(5)]


while i < 5:
	s[i] = int(raw_input('please enter a number:'))
	i += 1
	

print sum(s)


