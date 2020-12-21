'''
Random implementation of Tic Tac Toe with Python

Author: Keivan Ipchi Hagh
Year: 2020
License: MIT License
Follow me for more (https://github.com/keivanipchihagh)
'''

from random import choice

class Random:
	''' Implementation is somewhat Object-Oriented for reusability - Implementation supports bigger boards for fancy scenarios '''

	def __init__(self):
		''' Constructor '''

		# Variables initialization
		self.board = None


	def get_empty_cells(self):
		''' Returns a list of empty cells (Available moves) '''

		empty_cells = []
        
		for x, row in enumerate(self.board):
			for y, cell in enumerate(row):
				if cell == 0:
					empty_cells.append([x, y])

		return empty_cells


	def get_move(self, board):
		''' Gets a random possible move '''

		self.board = board

		return choice(self.get_empty_cells())