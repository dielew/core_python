#!/usr/bin/env python

def blank_omit(string_name):

	for i in range(len(string_name)):
		if string_name[i] == ' ':
			pass
		else:
			string_noblank_frleft = string_name[i:]
			break

	for j in range(-1, -len(string_noblank_frleft), -1):
		if string_noblank_frleft[j] == ' ':
			pass
		else:
			j += 1
			string_noblanks = string_noblank_frleft[:j]
			break
	return string_noblanks



if __name__ == '__main__':
	string_list = raw_input('Please enter a string which with blanks before, after and within the words:')
	string_noblanks = blank_omit(string_list)
	original_string_length = len(string_list)
	processed_string_length = len(string_noblanks)
	print 'The string without ends-blanks is:%s\nThe length of original string is:%d\nThe length of processed string is:%d ' %(string_noblanks, original_string_length, processed_string_length)
