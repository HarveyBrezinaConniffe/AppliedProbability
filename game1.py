import random as rand
import helpers

def simulateOneGame():
	slot = rand.randint(0, 36)
	if slot != 0 and slot%2 == 0:
		return 1, 1
	return -1, 1

helpers.simulateGame(simulateOneGame, 10000)
