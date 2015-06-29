#!/usr/bin/env python

def blank_omit(string_name):

	for i in range(len(string_name)):
		if string_name[i] == ' ':
			pass
		else:
			string_noblank_frleft = string_name[i:]
			break
	return string_noblank_frleft



if __name__ == '__main__':
	string_list = raw_input('Please enter a string which with blanks before, after and within the words:')
	string_no_left_blanks = blank_omit(string_list)
	string_leftblanks_reverse = string_no_left_blanks[::-1]
	string_no_endblanks_rev = blank_omit(string_leftblanks_reverse)
	string_no_endblanks = string_no_endblanks_rev[::-1]
	original_string_length = len(string_list)
	processed_string_lenth = len(string_no_endblanks)
	print 'The string without ends-blanks is:%s\nThe length of original string is:%d\nThe length of processed string is:%d ' %(string_no_endblanks, original_string_length, processed_string_lenth)
