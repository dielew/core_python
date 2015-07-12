#!/usr/bin/env python

# to implement the summation and product of two 2*2 matrix with list comprehension


print 'enter elements of Matrix A'
Ma_00 = int(raw_input('Enter the element of first row, first column: '))
Ma_01 = int(raw_input('Enter the element of first row, second column: '))
Ma_10 = int(raw_input('Enter the element of second row, first column: '))
Ma_11 = int(raw_input('Enter the element of second row, second column: '))

M_A = [[Ma_00, Ma_01], [Ma_10, Ma_11]] 

print 'enter elements of Matrix B'
Mb_00 = int(raw_input('Enter the element of first row, first column: '))
Mb_01 = int(raw_input('Enter the element of first row, second column: '))
Mb_10 = int(raw_input('Enter the element of second row, first column: '))
Mb_11 = int(raw_input('Enter the element of second row, second column: '))

M_B = [[Mb_00, Mb_01], [Mb_10, Mb_11]]

M_summation = [[(M_A[r][c] + M_B[r][c]) for c in range(len(M_A[0]))] for r in range(len(M_A))]

M_product = [[(M_A[r][0] * M_B[0][c] + M_A[r][1] * M_B[1][c]) for c in range(len(M_A[0]))] for r in range(len(M_A))]

print 'Matrix A: ', M_A
print 'Matrix B: ', M_B

print 'the summation of Matrix A and Matrix B is: ', M_summation
print 'the product of Matrix A times Matrix B is: ', M_product


