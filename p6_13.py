#!/usr/bin/env python 

# An implemention of the function atoc():
# The func takes string representation of a complex number, ends with imagine num notation 'j', as parameter.
# The func returns the related object of complex number
# build-in func ccomplex() is acceptable as complex():complex(real, imag), func eval() is banned.

def img_index(com_string):    # func img_index returns the very index of the sign notation of imaginary part
	oper_str = ''
	ind = 0
	counter = 0

	for oper in complex_str:
		if oper in '+-e':
			oper_str += oper  # acquire all the notations in one string, in the same order

	if oper_str[0] == 'e':
		opi = 2
	elif oper_str[0:2] == '-e':
		opi = 3
	elif oper_str[0] == '-' and len(oper_str) != 1:
		opi = 1
	else:
		opi = 0

	while counter <= opi:    # variable ind inc 1 than required ,before loop exits. Returned value should dec 1  
		if complex_str[ind] in oper_str:
			counter += 1
		ind += 1
	return  ind - 1


if __name__ == '__main__':
	complex_str_with_j = raw_input('Enter a complete string of a complex number:  ')
	complex_str = complex_str_with_j[:-1]    # omitting notation 'j' of the string, ready for passing, as argument
	img_index = img_index(complex_str) 
	real_str = complex_str[:img_index]
	img_str = complex_str[img_index:]

	complex_num = complex(float(real_str), float(img_str))  # complex() builtin fuctions as required
	print 'The complex number you have just entered is: \n', complex_num
