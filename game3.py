import random as rand
import helpers

def game3():
    
    betAmount = 1
    count = 0
    balance = 0
    while balance <= 10 and betAmount <= 100:
        amountWon = 0
        balance -= betAmount
        count += 1
        slot = rand.randint(0,36)
        if slot != 0 and slot%2 == 0:
            amountWon += betAmount*2
            betAmount = 1
        else:
            betAmount *= 2
        balance += amountWon
    
    return balance, count


winnings, playTimes = helpers.simulateGame(game3, 10000)
helpers.printStats(winnings, playTimes)
# Plot avg and variance of winnings
helpers.plotAvgAndVariance(winnings, "Avg and variance of winnings")
# Plot avg and variance of proportion of wins
propOfWins = list(map(int, (x > 0 for x in winnings)))
helpers.plotAvgAndVariance(propOfWins, "Avg and variance of proportion of wins")
