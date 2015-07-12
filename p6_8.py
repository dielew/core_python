#!/usr/bin/env python


digit_words = ['null', 'eins', 'zwei', 'drei', 'viel', 'fuenf', 'sechs', 'sieben', 'acht', 'neun']

input_int_str = raw_input('Please enter a integer number:')



for i in input_int_str:
	index_int = int(i)
	print digit_words[index_int],

