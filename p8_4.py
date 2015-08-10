#!/usr/bin/env python


def isprime(num):
	if num == 2:
		return True
	else:
		ispri = False
		divisor = num / 2 + 1
		for i in range(divisor, 1, -1):
			if num % i != 0:
				ispri = True
			else:
				ispri = False
				break
		return ispri

if __name__ == '__main__':
	num = int(raw_input('Please enter a integer num: '))
	print "%d is a prime number, that is" %(num), isprime(num)
