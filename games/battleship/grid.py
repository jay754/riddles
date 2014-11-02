from exceptions import *

#Grid Class
class Board:
	Y_SIZE = 10 #size of the y axis
	X_SIZE = 10 #size of the x axis

	def __init__(self):
		self.grid = []
		self.boats = {}

	def set_grid(self):
		for y in range(Y_SIZE):
			self.grid.append([])
			for x in range(X_SIZE):
				self.grid[y].append("*")

		return self.grid

	def boats(self):
		self.boats = {"cruiseship": 1,
                      "airship": 2,
                      "longship": 3,
                      "fourship": 4,
                      "battleship": 5}

		return self.boats

	def get_boat_size(self, choice):
		boat = None

		if choice is not None:
			if choice in self.boats().keys():
				boat = self.boats()[choice]
			elif choice not in self.boats().keys():
				raise Exception("Wrong Error Pick Again")

		return boat

	def location(self, y, x):
		if y == None or x == None:
			return -1

		if y is not None and x is not None:
			return (y, x)

	def place_boat(self, boat, g, location):
		Ship = ""

		if boat is None or g is None or location is None:
			return -1

		if != None:
			y = location[0]
			x = location[1]

		if boat is not None:
			if int(boat) == 1:
				Ship += "C"
			elif int(boat) == 2:
				Ship += "A"
			elif int(boat) == 3:
				Ship += "L"
			elif int(boat) == 4:
				Ship += "F"
			elif int(boat) == 5:
				Ship += "B"

		if g is not None or location is not None:
			for i range(boat):
				g[y+i][x] = Ship

	def print_grid(self, board):
		if board is not None:
			for i in range(len(board)):
				print " ".join(board[i])