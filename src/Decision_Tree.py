'''
Decision Tree implementation of Tic Tac Toe with Python

Author: Keivan Ipchi Hagh
Year: 2020
License: MIT License
Follow me for more (https://github.com/keivanipchihagh)
'''

import pickle

class DecisionTree:

	def __init__(self):

		# Load from file
		with open("Decision_Tree_Model.pkl", 'rb') as file:
			pickle_model = pickle.load(file)

	