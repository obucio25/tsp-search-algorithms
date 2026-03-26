import numpy as np

def greedy(board):
    numCities = len(board)
    visited = np.zeros(numCities, dtype=int)
    visited[0] = 1 #mark starting city as visited so it is ignored
    currCity = 0
    cost = 0
    
    for i in range(numCities):
        minCost = 1000 #higher than max cost (100)
        
        for j in range(numCities): #find smallest cost
            if (not visited[j]) and (board[currCity][j] < minCost):
                minCost = board[currCity][j]
                nextCity = j
        
        visited[nextCity] = True
        cost += board[currCity][nextCity]
        currCity = nextCity
        
    cost += board[currCity][0]
    
    return cost
