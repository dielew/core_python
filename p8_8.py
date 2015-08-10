#!/usr/bin/env python


def factorial(num_factorial):
	product = 1
	for num_each in range(2, num_factorial + 1):
		product *= num_each
	return product


if __name__ == '__main__':
	prompt = 'Pleas enter a postive integer: '
	num_int = int(raw_input(prompt))
	if num_int > 0:
		result = factorial(num_int)
		print 'The factorial value of %d is: %d ' %(num_int, result)
	else:
		print 'invalid value, num input should be positive integer'

