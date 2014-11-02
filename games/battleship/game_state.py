from exceptions import *
from grid import Board

class player_state:
	def __init__(self):
		self.cruiseship = False 
		self.airship = False 
		self.longship = False
		self.fourship = False
		self.battleship = False

	def player_state(self, grid):
		pass

	def check_game(self):
		if self.cruiseship and self.airship and self.longship and self.fourship and self.battleship:
			return "You have won the game Congrants"

class computer_state(player_state):
	def __init__(self):
		pass

	def state(self):
		pass