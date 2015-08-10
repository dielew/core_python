#!/usr/bin/env python

def fabonacci(nth_fab):
	fab_list = []
	fab_list.append(1)
	fab_list.append(1)

	for fab_ith in range(2, nth_fab):
		fab_list.append(fab_list[fab_ith - 1] + fab_list[fab_ith - 2])
	
	return fab_list[nth_fab - 1]

if __name__ == '__main__':
	prompt = 'Input the Xth, get the Xth fabonacci number:'
	n_th = int(raw_input(prompt))
	print 'the %d th fabonacci number is: %d' %(n_th, fabonacci(n_th))
