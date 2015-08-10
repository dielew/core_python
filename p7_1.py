#!/usr/bin/env python

dic_a = {'one':1, 'three':3, 'five':5, 'seven':7, 'nine':9}
dic_b = {'zero':0, 'two':2, 'four':4, 'six':6, 'eight':8}
new_dic = { }
new_dic_key = [ ]
new_dic_value = [ ]

for keys in dic_a:
	new_dic_key.append(keys)
	new_dic_value.append(dic_a[keys])	
for keys in dic_b:
	new_dic_key.append(keys)
	new_dic_value.append(dic_b[keys])	

new_dic = dict(zip(new_dic_key, new_dic_value))

print dic_a
print dic_b
print new_dic
