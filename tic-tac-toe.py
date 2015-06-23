player = ('x','o')
num_moves_made = 0
location = range(9)		#[0,1,2,3,4,5,6,7,8]
# Draw the grid
def draw_board(moves):
	print " %s | %s | %s " % (moves[0], moves[1], moves[2])
	print "-----------"
	print " %s | %s | %s " % (moves[3], moves[4], moves[5])
	print "-----------"
	print " %s | %s | %s " % (moves[6], moves[7], moves[8])

draw_board(location)

# # Ask the user where they want to move
# move = int(raw_input("Player x, where do you want to move? "))

# # The computer redraws the board with the X where the user said
# location[move] = 'x'
# draw_board(location)

# # Ask the second user where they want to move
# move = int(raw_input("Player o, where do you want to move? "))

# # The computer redraws the board with the O where the user said (the x still on the board)
# location[move] = 'o'
# draw_board(location)

# Repeat steps until...
	# Until someone wins (horiz, vert, diag)
	#  --or--
	# All the spaces are filled up
# while(not no_winner() or not board_full()):
while(True):
	# Ask the user where they want to move
	move = int(raw_input("Player %s, where do you want to move? " % (player[num_moves_made%2])))

	# The computer redraws the board with the X where the user said
	location[move] = player[num_moves_made%2]
	num_moves_made += 1
	draw_board(location)

# If someone won:
	# Print "[letter] wins!"
# Else:
	# Print "draw!"
# Exit the program