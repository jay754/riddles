from exceptions import *
from grid import *

#stats class
class Stats:
	def __init__(self):
		self.player_moves = []
		self.computer_moves = []

	def player_moves_add(self, player_move):
		""" Added Players moves """

		if player_move is not None:
			self.player_moves.append(player_move)

	def computer_moves_add(self, computer_move):
		""" Added Computer moves """

		if computer_move is not None:
			self.computer_moves.append(computer_move)

	def get_player_moves(self):
		return self.player_moves

	def get_computer_moves(self):
		return self.computer_moves

	def get_amount_player_turns(self):
		return len(self.player_moves)

	def get_amount_computer_turns(self):
		return len(self.computer_moves)

	def combined_turns(self):
		return self.get_amount_player_turns() + self.get_amount_computer_turns()