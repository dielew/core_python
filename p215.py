#!/usr/bin/env python

one = float(raw_input('enter the 1st number:'))
two = float(raw_input('enter the 2nd number:'))
tre = float(raw_input('enter the 3rd number:'))


if (one <= two):
	p1 = one
	p2 = two
else:
	p1 = two
	p2 = one

if p1 <= tre:
	p1e = p1
	if p2 <= tre:
		p2e = p2
		p3e = tre
	else:
		p2e = tre
		p3e = p2
else:
	p1e = tre
	p2e = p1
	p3e = p2

print p1e, p2e, p3e

