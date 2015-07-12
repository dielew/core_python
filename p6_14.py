#!/usr/bin/env python

import random

# to implement a Rochambeau game without 'if' control

print '''                 ROCHAMBEAU GAME

Description: Player could type one number for picking card after prompt, options are:
	        '1' for  Rock
	        '2' for  Paper
	        '3' for  Scissor
	         otherwise is invalid valid, for Exit.
'''

token = {1:'Rock', 2:'Paper', 3:'Scissor'}
result_lookup = {0:'Even', 1:'You win', -1:'Computer wins', 2:'Computer wins', -2:'You win'}

while True:
	computer = random.randint(1, 3)
	player_in = raw_input('Pick your card(Enter [1]: Rock, [2]: Paper, [3]: Scissor): ')
	while (player_in == '1' or player_in == '2' or player_in == '3'):
		player = int(player_in)
		break
	else:
		print 'Value_Err, valid value should be one integer between 1 and 3!' 
		break

	result_value = player - computer
	print 'computer:             ', token[computer]
	print 'player:               ', token[player]
	print 'winner of this round: ', result_lookup[result_value]
	
	


