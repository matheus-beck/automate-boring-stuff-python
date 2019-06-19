# This program is a tic tac toe game.

def print_board(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
	
def check_winner(board, turn):
	return ((board['top-L'] == turn and board['top-M'] == turn and board['top-R'] == turn) or # across the top
			(board['mid-L'] == turn and board['mid-M'] == turn and board['mid-R'] == turn) or # across the middle
			(board['low-L'] == turn and board['low-M'] == turn and board['low-R'] == turn) or # across the bottom
			(board['top-L'] == turn and board['mid-L'] == turn and board['low-L'] == turn) or # down the left side
			(board['top-M'] == turn and board['mid-M'] == turn and board['low-M'] == turn) or # down the middle
			(board['top-R'] == turn and board['mid-R'] == turn and board['low-R'] == turn) or # down the right side
			(board['top-L'] == turn and board['mid-M'] == turn and board['low-R'] == turn) or # diagonal
			(board['top-R'] == turn and board['mid-M'] == turn and board['low-L'] == turn))   # diagonal
	
board = {'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ',
		 'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',
		 'low-L' : ' ', 'low-M' : ' ', 'low-R' : ' '}

turn = 'X'

print_board(board)

for i in range(9):
	print('Turn for ' + turn + '. Move on which space?')
	print('Avaiable spaces: top-L, top-M, top-R, mid-L, mid-M, mid-R, low-L, low-M, low-R')
	
	move = input()
	
	while move not in board.keys():
		print('You typed a non valid space! Try again:')
		move = input()
		
	board[move] = turn
	
	if check_winner(board, turn):
		print(turn + ' is the winner!')
		print_board(board)
		break
	
	turn = ('O' if turn == 'X' else 'X')
	
	print_board(board)
	
	if i == 8:
		print ('It is a draw!')