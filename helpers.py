import matplotlib.pyplot as plt

def simulateGame(game, iterations):
	winnings = []
	playTimes = []
	for i in range(iterations):
		winning, playTime = game()
		winnings.append(winning)
		playTimes.append(playTime)
	return winnings, playTimes

def printStats(winnings, playTimes):
	# Expected winnings
	expectedWinnings = 0
	for winning in winnings:
		expectedWinnings += winning
	expectedWinnings /= len(winnings)
	winningsVariance = getVariance(winnings, expectedWinnings)

	# Proportion of wins
	winsAndLosses = []
	wins = 0
	for winning in winnings:
		if winning > 0:
			winsAndLosses.append(1)
			wins += 1
		else:	
			winsAndLosses.append(0)
	winProportion = wins/len(winnings)
	winProportionVariance = getVariance(winsAndLosses, winProportion)

	# Expected playing time
	playingTime = 0.
	for playTime in playTimes:
		playingTime += playTime
	playingTime /= len(playTimes)
	playingTimeVariance = getVariance(playTimes, playingTime)

	# Maximum loss
	maxLoss = abs(min(winnings))

	# Maximum win
	maxWin = max(winnings)

	print("Expected winnings: {}".format(expectedWinnings))
	print("Expected winnings variance: {}".format(winningsVariance))
	print("Proportion of games won: {}".format(winProportion))
	print("Proportion of games won variance: {}".format(winProportionVariance))
	print("Expected playing time per game: {}".format(playingTime))
	print("Playing time variance: {}".format(playingTimeVariance))
	print("Maximum loss: ${}".format(maxLoss))
	print("Maximim win: ${}".format(maxWin))

def getMean(arr):
	total = 0
	for item in arr:
		total += item
	return total/len(arr)

def getVariance(arr, mean):
	total = 0
	for item in arr:
		total += (item-mean)**2
	return total/(len(arr)-1)			

def plotAvgAndVariance(arr):
	runningAvgs = []

	runningVariances = []

	for i in range(2, len(arr)+1):
		avg = getMean(arr[0:i])
		var = getVariance(arr[0:i], avg)
		
		runningVariances.append(avg)
		runningAvgs.append(var)
	
	plt.plot(runningAvgs, label="Average")
	plt.plot(runningVariances, label="Variance")
	plt.title("Avg and variance")
	plt.legend()
	plt.xlabel("Iteration")
	plt.show()
