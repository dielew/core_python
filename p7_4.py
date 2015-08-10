#!/usr/bin/env python

import keyword

key_list = range(5)
value_list = keyword.kwlist[:5]
dic = {}
out_dic = {}

for i in range(len(key_list)):
	dic = {}.fromkeys(key_list[i:], value_list[i])
	out_dic.update(dic)


print 'one list is ', key_list
print 'another list is', value_list
print 'the output is', out_dic 

