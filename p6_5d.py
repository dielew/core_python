#!/usr/bin/env python


std_input_string = raw_input('Please input a string, we give you back a palindrome: ')

rev_start = len(std_input_string) - 1

string_rev = std_input_string[0:rev_start]

string_rev_done = string_rev[::-1]

string_palindrome = std_input_string + string_rev_done

print string_palindrome
