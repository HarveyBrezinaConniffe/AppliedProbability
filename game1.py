import random as rand

def simulateOneGame():
	slot = rand.randint(0, 36)
	if slot != 0 and slot%2 == 0:
		return 1
	return -1

# Simulate 10,000 games
winnings = []
for i in range(10000):
	winnings.append(simulateOneGame())

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
playingTime = 1

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
