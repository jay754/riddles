from exceptions import *
from grid import Board

class State:
	def __init__(self):
		self.cruiseship = False 
		self.airship = False 
		self.longship = False
		self.fourship = False
		self.battleship = False

class Player_State(State):
	def __init__(self):
		pass

	def state(self):
		pass 

class Computer_state(State):
	def __init__(self):
		pass

	def state(self):
		pass