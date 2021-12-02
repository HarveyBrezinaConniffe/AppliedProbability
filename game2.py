import random as rand
import helpers

def game2():
	slot = rand.randint(0, 36)
	if slot != 0 and slot == 22:
		return 35, 1
	return -1, 1

winnings, playTimes = helpers.simulateGame(game2, 10000)
helpers.printStats(winnings, playTimes)
helpers.plotAvgAndVariance(winnings, "Avg and variance of winnings")

propOfWins = list(map(int, (x > 0 for x in winnings)))
helpers.plotAvgAndVariance(propOfWins, "Avg and variance of proportion of wins")
