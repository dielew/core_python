#!/usr/bin/env python

def strprt_order(stri):
	i = 0
	while (i < len(stri)):
		print stri[i]
		i += 1


def strprt_rev(stri):
	i = len(stri) - 1
	while (i >= 0):
		print stri[i]
		i -= 1


if __name__ == '__main__':
	inp_str = raw_input('Please input a string:')
	strprt_order(inp_str)
	strprt_rev(inp_str)

