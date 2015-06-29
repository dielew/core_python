#!/usr/bin/env python

def gcd(num_a, num_b):
	while num_a % num_b != 0:
		remain = num_a % num_b
		num_a = num_b
		num_b = remain
	gcd = num_b
	return gcd

def lcm(num_a, num_b):
	product = num_a * num_b
	while num_a % num_b != 0:
		remain = num_a % num_b
		num_a = num_b
		num_b = remain
	gcd = num_b
	lcm = product / gcd
	return lcm

if __name__ == '__main__':
	while True:
		num_a = int(raw_input('Enter the first number, type should be int: '))
		num_b = int(raw_input('Enter the second number, type should be int: '))
		print '''
		The Greatest Common Divisor of %d and %d is: %d
		The Least Common Multiple of  %d and  %d is: %d
		''' %(num_a, num_b, gcd(num_a, num_b), num_a, num_b, lcm(num_a, num_b))
