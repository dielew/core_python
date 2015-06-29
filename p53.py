#!/usr/bin/env python

while True:
	score = int(raw_input("Enter your score, should be a integer between 0 and 100:"))

	if (score <= 100 and score >= 90):
		mark = 'A'
	elif (score <= 89 and score >= 80):
		mark = 'B'
	elif (score <= 79 and score >= 70):
		mark = 'C'
	elif (score <= 69 and score >= 60):
		mark = 'D'
	elif (score < 60 and score >= 0):
		mark = 'F'
	else:
		mark = 'Invalid Score Range'

	print "Your Mark is %s" %(mark)
	

