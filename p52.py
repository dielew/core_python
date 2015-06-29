#!/usr/bin/env python


def product(a, b):
	return float(a * b)

if __name__ == '__main__':
	a = float(raw_input('enter a number:'))
	b = float(raw_input('enter a number:'))
	print "the product of a and b is %f" %(product(a, b))

