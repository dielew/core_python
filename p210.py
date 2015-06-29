

numb = float(raw_input('Enter a num which value is between 1 and 100, otherwise is invalid:'))

if (numb > 100 or numb < 1):
	print 'invalid number, should be 1~100'
	while (numb > 100 or numb < 1):
		print 'invalid number, should be 1~100' 
		numb = float(raw_input('Enter a num which value is between 1 and 100, otherwise is invalid:'))
else:
    print 'valid number'

print 'valid number'
