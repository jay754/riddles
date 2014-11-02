from exceptions import *
from grid import Board
from game_state import *

def placeBoats(choice, x, y):
	boat = None

	if choice is not None:
		if choice in boats().keys():
			boat = boats()[choice]
		elif choice not in boats().keys():
			raise Exception("Wrong Error Pick Again")

	return (boat, x, y)

def printGrid(show, g):
	for i in range(len(g)):
		print " ".join(g[i])

def main():
	print Board().boats()
	print Board().set_grid()

main()