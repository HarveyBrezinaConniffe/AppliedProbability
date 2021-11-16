def simulateGame(game, iterations):
	winnings = []
	playTimes = []
	for i in range(iterations):
		winning, playTime = game()
		winnings.append(winning)
		playTimes.append(playTime)
	printStats(winnings, playTimes)

def printStats(winnings, playTimes):
	# Expected winnings
	expectedWinnings = 0
	for winning in winnings:
		expectedWinnings += winning
	expectedWinnings /= len(winnings)

	# Proportion of wins
	wins = 0
	for winning in winnings:
		if winning > 0:
			wins += 1
	winProportion = wins/len(winnings)

	# Expected playing time
	playingTime = 0
	for playTime in playTimes:
		playingTime += playTime
	playingTime /= len(playTimes)

	# Maximum loss
	maxLoss = abs(min(winnings))

	# Maximum win
	maxWin = max(winnings)

	print("Expected winnings: {}".format(expectedWinnings))
	print("Proportion of games won: {}".format(winProportion))
	print("Expected playing time per game: {}".format(playingTime))
	print("Maximum loss: ${}".format(maxLoss))
	print("Maximim win: ${}".format(maxWin))
