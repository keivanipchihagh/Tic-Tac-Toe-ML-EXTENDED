'''
Intractive interface for debugging and testing purposes

Author: Keivan Ipchi Hagh
Year: 2020
License: MIT License
Follow me for more (https://github.com/keivanipchihagh)
'''

# AI algorithm
from MiniMax import MiniMax
from Random import Random

from os import system
import platform

# For multi-threading purposes
import os
import threading


class TicTacToe:
	''' Tic Tac Toe Interface implementation '''

	def __init__(self, dimention):
		''' Constructor '''
		self.board = [ [0 for j in range(dimention)] for i in range(dimention) ]


	def clean(self):
		''' Clears the console '''
		system('cls') if ('windows' in platform.system().lower()) else system('clear')		


	def print(self):
		''' Prints a fancy board '''

		self.clean()

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


	def get_user_input(self):
		''' Gets an input from user '''

		while True:
			user_input = int(input('Choose a cell (1-9): '))

			x, y = (user_input // 3) if (user_input % 3 != 0) else (user_input // 3 - 1), 2 if (user_input % 3 == 0) else (user_input % 3 - 1)

			if [x, y] in self.get_empty_cells():
				return (x, y)


	def get_empty_cells(self):
		''' Returns whether board has any empty cells or not '''

		empty_cells = []
        
		for x, row in enumerate(self.board):
			for y, cell in enumerate(row):
				if cell == 0:
					empty_cells.append([x, y])

		return empty_cells


	def is_move_available(self):
		''' Returns whether board has any empty cells or not '''

		return len(self.get_empty_cells()) != 0


	def wins(self, AI, HUMAN):
		''' This function determines whether a player wins for not - Returns +1 if AI has won & -1 if HUMAN has won '''

		# Check rows
		for row in self.board:
			if row.count(AI) == len(self.board):
				return +1
			elif row.count(HUMAN) == len(self.board):
				return -1

		# Check columns
		for i in range(len(self.board)):
			column = [row[i] for row in self.board]

			if column.count(AI) == len(self.board):
				return +1
			elif column.count(HUMAN) == len(self.board):
				return -1

		# Check diagonals
		diagonal_1 = [self.board[i][i] for i in range(len(self.board))]
		diagonal_2 = [self.board[len(self.board) - i - 1][i] for i in range(len(self.board) - 1, -1, -1)]

		if diagonal_1.count(AI) == len(self.board) or diagonal_2.count(AI) == len(self.board):
			return +1
		elif diagonal_1.count(HUMAN) == len(self.board) or diagonal_2.count(HUMAN) == len(self.board):
			return -1

		return None # No winner


	def game_state(self, AI, HUMAN):
		''' Determines whether any of the players has won the game '''

		win_state = self.wins(AI, HUMAN)

		if win_state == +1:
			self.print()
			print('AI won!')			
			return True

		elif win_state == -1:
			self.print()
			print('User won!')
			return True

		elif not self.is_move_available():
			self.print()
			print('Draw!')
			return True

		else:
			return False	
			

	def play(self, algorithm, user_first):
		''' Main game loop '''

		turn = -1 if (user_first) else 1

		while self.is_move_available():
    			
			# Print board
			self.print()

			# Get move
			move = algorithm.get_move(self.board) if (turn == 1) else self.get_user_input()

			# Apply move
			self.board[move[0]][move[1]] = turn			

			# Check game state
			if self.game_state(1, -1):
				break

			# Switch turn
			turn *= -1


def __main__():
	''' Main driver function '''

	# Main game engine
	tictactoe = TicTacToe(3)

	# AI algorithm
	algorithm = MiniMax()
	# algorithm = Random()

	while True:
		starting_user = input('Wanna start first? [y/n]: ')

		if starting_user in ['y', 'n']:
			tictactoe.play(algorithm, True if (starting_user == 'y') else False)
			break


# Call driver function
__main__()