'''
MiniMax implementation of Tic Tac Toe with Python

Author: Keivan Ipchi Hagh
Year: 2020
License: MIT License
Follow me for more (https://github.com/keivanipchihagh)
'''

# Imports
from math import inf as infinity
from random import choice

class MiniMax:
    ''' Implementation is somewhat Object-Oriented for reusability - Implementation supports bigger boards for fancy scenarios '''

    def __init__(self):
        ''' Constructor '''

        # Variables initialization
        self.board = None

        self.HUMAN = -1
        self.HUMAN_score = -10

        self.AI = +1
        self.AI_score = 10


    def evaluate(self):
        ''' Heuristic evaluation of game state. Rewards the AI if it wins '''

        if self.wins(self.AI) == +1:
            return self.AI_score              # Reward the AI if it outruns the opponent
        elif self.wins(self.HUMAN) == -1:
            return self.HUMAN_score           # Punish the AI if it is outran by the opponent
        else:
            return 0                        # Draw


    def wins(self, player):
        ''' This function determines whether a player wins for not - Returns +1 if AI has won & -1 if HUMAN has won '''

        # Check rows
        for row in board:
            if row.count(self.AI) == len(board):
                return +1
            elif row.count(self.HUMAN) == len(board):
                return -1

        # Check columns
        for i in range(len(board)):
            column = [row[i] for row in board]

            if column.count(self.AI) == len(board):
                return +1
            elif column.count(self.HUMAN) == len(board):
                return -1

        # Check diagonals
        diagonal_1 = [board[i][i] for i in range(len(board))]
        diagonal_2 = [board[len(board) - i - 1][i] for i in range(len(board) - 1, -1, -1)]

        if diagonal_1.count(self.AI) == len(board) or diagonal_2.count(self.AI) == len(board):
            return +1
        elif diagonal_1.count(self.HUMAN) == len(board) or diagonal_2.count(self.HUMAN) == len(board):
            return -1

        return None # No winner


    def is_game_over(self):
        ''' Determines whether any of the players has won the game '''

        return self.wins(self.AI) == +1 or self.wins(self.HUMAN) == -1


    def get_empty_cells(self):
        ''' Returns a list of empty cells (Available moves) '''

        empty_cells = []
        
        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                if cell == 0:
                    empty_cells.append([x, y])

        return empty_cells


    def minimax(self, depth, player):
        ''' The brain of the AI, which moves the best possible move '''

        score = self.evaluate()
        empty_cells = self.get_empty_cells()

        # We have a winner, return it's score
        if score in [self.AI_score, self.HUMAN_score]:
            return score
        # Draw?
        elif len(empty_cells) == 0:
            return 0

        # Set best score
        best_score = -10 if (player == self.AI) else +10

        for cell in empty_cells:

            # Get cell coordinates
            x, y = cell[0], cell[1]

            # Temporarily set the move
            board[x][y] = player

            # Recalculate best move by recursively going down the tree - To make our AI smarter we want to win faster so Depth is important here!
            if player == self.AI:
                best_score = max(best_score, self.minimax(depth + 1, -player)) - depth
            else:
                best_score = min(best_score, self.minimax(depth + 1, -player)) + depth

            # Reset the move back to it's original state
            board[x][y] = 0

        return best_score


    def get_move(self, board):
        ''' Gets the best possible move using the algorithm '''

        # Set the board
        self.board = board        

        best_score = -infinity        
        best_move = tuple()

        empty_cells = self.get_empty_cells()

        # Choose random if it's the first move
        if len(empty_cells) == 9:
            return choice([0, 1, 2]), choice([0, 1, 2])

        for cell in empty_cells:

            x, y = cell[0], cell[1]

            board[x][y] = self.AI

            move_score = self.minimax(0, self.HUMAN)

            board[x][y] = 0

            # Compare to see if current move is better
            if move_score > best_score:
                best_score, best_move = move_score, (x, y)
        
        return best_move