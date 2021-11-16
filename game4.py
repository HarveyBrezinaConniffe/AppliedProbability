import random as rand

def simulateOneGame():
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

# Simulate 10,000 games
winnings = []
playTimes = []
for i in range(10000):
	winning, playTime = simulateOneGame()
	winnings.append(winning)
	playTimes.append(playTime)

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

print("Game 1:")
print("Expected winnings: {}".format(expectedWinnings))
print("Proportion of games won: {}".format(winProportion))
print("Expected playing time per game: {}".format(playingTime))
print("Maximum loss: ${}".format(maxLoss))
print("Maximim win: ${}".format(maxWin))
