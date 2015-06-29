#!/usr/bin/env python

import random

num = [ ]
for i in range(5):
	num.append(random.randint(0, 10))

def sigma():
	return sum(num)

def aver():
	return sum(num)/5.0

CMD = {'s': sigma, 'a': aver}

def showmenu():
	print 'Numbers are %d  %d  %d  %d  %d' %(num[0], num[1], num[2], num[3], num[4])
	print '''
			Please select the option:
			NOTICE: your input should be ONE LOWERCASE letter

			(S)um
			(A)verage
			(Q)uit
	'''
	while True:
		func = raw_input('Your selection is:')
		if func == 'q':
			break
		else:
			result = CMD[func]()
			print 'Your selection is %s, result is %f' %(func, result) 

if __name__ == '__main__':
	showmenu()
