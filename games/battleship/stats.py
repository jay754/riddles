from exceptions import *
from grid import *

#stats class
class stats:
	def __init__(self):
		self.player_moves = []
		self.computer_moves = []
		self.number_of_player_turns = 0
		self.number_of_computer_turns = 0

	def player_moves_add(self, player_move):
		self.player_moves.append(player_move)

	def computer_moves_add(self, computer_move):
		self.computer_moves.append(computer_move)

	def get_player_moves(self):
		return self.player_moves

	def get_computer_moves(self):
		return self.computer_moves

	def add_player_turns(self):
		self.number_of_player_turns += 1

	def add_player_turns(self):
		self.number_of_computer_turns += 1

	def combined_turns(self):
		return self.number_of_player_turns + self.number_of_computer_turns