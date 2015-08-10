#!/usr/bin/env python

def getfactors(num_int):
	if num_int > 0:
		factor_list = []
		divisor = num_int / 2 + 1
		for fac in range(1, divisor):
			if num_int % fac == 0:
				factor_list.append(fac)
			else:
				pass
		factor_list.append(num_int)
	else:
		return []
	return factor_list

if __name__ == '__main__':
	prompt = 'Please enter a positive integer number: '
	num_int = int(raw_input(prompt))
	print 'Factors of number %d is/are:' %num_int, getfactors(num_int)
