import numpy as np
import math
import random

#Sums up 
def routeCost(board, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += board[path[i]][path[i + 1]]
    return cost

def simulatedAnnealing(board, initialTemp=1000, coolingRate=0.995, minTemp=1):
    numCities = len(board)

    # Start with a random permutation of cities (excluding city 0 at start/end)
    middle = list(range(1, numCities))
    random.shuffle(middle)
    currentPath = [0] + middle + [0]
    currentCost = routeCost(board, currentPath)

    bestPath = currentPath[:]
    bestCost = currentCost

    temp = initialTemp

    while temp > minTemp:
        # Pick two random positions in the middle of the path (indices 1..numCities-1)
        i, j = sorted(random.sample(range(1, numCities), 2))

        # Swap the two cities
        neighbor = currentPath[:]
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        neighborCost = routeCost(board, neighbor)

        delta = neighborCost - currentCost

        # Accept better solutions always; accept worse solutions probabilistically
        if delta < 0 or random.random() < math.exp(-delta / temp):
            currentPath = neighbor
            currentCost = neighborCost

        if currentCost < bestCost:
            bestPath = currentPath[:]
            bestCost = currentCost

        temp *= coolingRate

    return bestCost, bestPath
