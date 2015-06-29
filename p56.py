#!/usr/bin/env python

def splition():
	expr = raw_input('Please enter your expression: ')
	lenpow = len(expr.split('**'))
	if lenpow == 2:
		operator = '**'
		expr_operands = expr.split(operator)

	elif lenpow == 1:
		for i in '+-*/%':
			if len(expr.split(i)) == 2:
				operator = i
				expr_operands = expr.split(operator)
				break
	else:
		print 'invalid operator!'

	operand1 = float(expr_operands[0])
	operand2 = float(expr_operands[1])

	if operator == '+':
		result = summation(operand1, operand2)
	elif operator == '-':
		result = substraction(operand1, operand2)
	elif operator == '*':
		result = production(operand1, operand2)
	elif operator == '/':
		result = division(operand1, operand2)
	elif operator == '%':
		result = modulation(operand1, operand2)
	elif operator == '**':
		result = power(operand1, operand2)


	print 'your expr is: \n%f  %s  %f\nresult = %f' %(operand1, operator, operand2, result)

def summation(operand1, operand2):
	return operand1 + operand2
def substraction(operand1, operand2):
	return operand1 - operand2
def production(operand1, operand2):
	return operand1 * operand2
def division(operand1, operand2):
	return operand1 / operand2
def modulation(operand1, operand2):
	return operand1 % operand2
def power(operand1, operand2):
	return pow(operand1, operand2)
#	base = 1
#	for expon in range(int(operand2)):
#		base *= operand1
#	return base

if __name__ == '__main__':
	while True:
		splition()


