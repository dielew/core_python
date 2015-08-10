#!/usr/bin/env python

from p8_4 import isprime
from p8_5 import getfactors


if __name__ == '__main__':

	prompt = 'Please enter a positive integer: '
	inp_num = int(raw_input(prompt))

	fac_list = getfactors(inp_num)
	pri_factorization = []
	factorz = 2
	over_l = inp_num
	pri_fac_prodt = 1

	if isprime(inp_num) == True:
		pri_factorization = fac_list
	else:
		while pri_fac_prodt < inp_num:
			if isprime(factorz) == True:
				(over_res, rem) = divmod(over_l, factorz)
				if rem == 0:
					if over_res != 1:
						pri_factorization.append(factorz)
						pri_fac_prodt *= factorz
						over_l = over_res
					else:
						pri_factorization.append(factorz)
						break
				else:
					factorz +=1
			else:
				factorz += 1
			
	
	print 'The prime factorization result of %d is:' %(inp_num) ,pri_factorization 
			
	





