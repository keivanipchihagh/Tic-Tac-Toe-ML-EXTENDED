'''
Intractive interface for debugging and testing purposes

Author: Keivan Ipchi Hagh
Year: 2020
License: MIT License
Follow me for more (https://github.com/keivanipchihagh)
'''

class TicTacToe:
	''' Tic Tac Toe Interface implementation '''

	def __init__(self, dimention):
		''' Constructor '''

		self.board = [ [0 for j in range(dimention)] for i in range(dimention) ]


	def print(self):
		''' Prints a fancy board '''

		for i in range(len(self.board)):
			for j in range(len(self.board)):

				if self.board[i][j] == 0:
					print('   ', end = '')
				elif self.board[i][j] == 1:
					print(' X ', end = '')
				elif self.board[i][j] == -1:
					print(' O ', end = '')

				if j != len(self.board) - 1:
					print('|', end = '')

			if i != len(self.board) - 1:
				print('\n' + ("--- " * len(self.board)))
			else:
				print()


tictactoe = TicTacToe(3)
tictactoe.print()