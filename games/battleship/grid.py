from exceptions import *

#Grid Class
class Board:
	def __init__(self):
		self.grid = []
		self.boats

	def set_grid(self):
		for y in range(10):
			self.grid.append([])
			for x in range(10):
				self.grid[y].append("*")

		return self.grid

	def boats(self):
		self.boats = {"cruiseship": 1,
				 	  "airship": 2,
					  "longship": 3,
				 	  "fourship": 4,
				 	  "battleship": 5}

		return self.boats