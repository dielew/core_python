#!/usr/bin/env python



bigger_string = raw_input('Enter the big string:')
small_string = raw_input('Enter the small string:')

is_part_of = int(bigger_string.find(small_string))

if (is_part_of == -1):
	print '%s is NOT part of %s' %(small_string, bigger_string)

else:
	print '%s IS part of %s' %(small_string, bigger_string)
