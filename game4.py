import random as rand
import helpers

def game4():
	balance = 0
	playingTime = 0
	numberList = [1, 2, 3, 4]
	while True:
		if len(numberList) == 0:
			break

		if len(numberList) == 1:
			currentBet = numberList[0]
		else:
			currentBet = numberList[0]+numberList[-1]
			
		if currentBet > 100:
			break
		
		slot = rand.randint(0, 36)
		if slot != 0 and slot%2 == 0:
			balance += currentBet
			numberList = numberList[1:-1]
		else:
			balance -= currentBet
			numberList.append(currentBet)
		playingTime += 1

	return balance, playingTime

winnings, playTimes = helpers.simulateGame(game4, 10000)
helpers.printStats(winnings, playTimes)

helpers.plotAvgAndVariance(winnings, "avg and variance of winnings")

propOfWins = list(map(int, (x > 0 for x in winnings)))
helpers.plotAvgAndVariance(propOfWins, "Avg and variance of proportion of wins")
