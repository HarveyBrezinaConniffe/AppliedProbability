import random as rand
import helpers

def game1():
	slot = rand.randint(0, 36)
	if slot != 0 and slot%2 == 0:
		return 1, 1
	return -1, 1

winnings, playTimes = helpers.simulateGame(game1, 10000)
helpers.printStats(winnings, playTimes)
# Plot avg and variance of winnings
helpers.plotAvgAndVariance(winnings, "Avg and variance of winnings")
# Plot avg and variance of proportion of wins
propOfWins = list(map(int, (x > 0 for x in winnings)))
helpers.plotAvgAndVariance(propOfWins, "Avg and variance of proportion of wins")
