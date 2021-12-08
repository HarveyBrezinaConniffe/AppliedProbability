import random
import helpers
import numpy as np

def cardGame():
    cards = list(range(1, 101))
    random.shuffle(cards)            # create deck of 100 cards, shuffle them
    hits = 0                        
    for x in range(0,100):
        if cards[x] == x:   
            hits+=1
    return hits                      # return number of hits 

def main(): 
    dataSet = []
    for x in range(0, 10001):       
        dataSet.append(cardGame())   # add an instant of card game 10,000 times
    variance = np.var(dataSet)
    expectation = np.mean(dataSet)
    helpers.plotAvgAndVariance(dataSet, title="Avg and variance")
    print("The variance of the 10,000 repititions: " + str(variance))
    print("The expectation of the 10,000 repititions: " + str(expectation))

main()