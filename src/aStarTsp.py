import numpy as np # Don't need to, but if testing on it's own with the uncommented out code then it is needed there

def aStarTsp(board, startCity=0):
  numCities = len(board)
  completeMask = (1 << numCities) - 1 # Mask in the variable name means filter usually in some way to see what cities have been visited

  def heuristic(currNode, visitedMask):
    unvisited = [i for i in range(numCities) if not (visitedMask & (1 << i))]

    if not unvisited:
      return board[currNode][startCity]

    minEdgeCost = 10**10 # Note if values get larger than this it will break the heuristic cal.
    for i in range(numCities):
      for j in range(numCities):
        if i != j and board[i][j] > 0:
          minEdgeCost = min(minEdgeCost, board[i][j])

    return minEdgeCost * len(unvisited)

  priQueue = []
  startMask = (1 << startCity)
  priQueue.append((0, 0, startCity, startMask, [startCity])) # The variables of priQueue go (g score, f score, vistedMask currently, path currently taken)

  bestCosts = {}

  while priQueue:
    priQueue.sort(key=lambda x: x[0])
    f, g, currCity, visitedMask, path = priQueue.pop(0)

    if visitedMask == completeMask: # If all the visitedMask shows all cities have been visited then it automatically returns to the starting city
      if board[currCity][startCity] <= 0: # Just making sure no errors occur
        continue
      
      totalCost = g + board[currCity][startCity]
      print(f"Path: {path + [startCity]}")
      print(f"Total Cost: {totalCost}\n")
      return path + [startCity], totalCost

    bestCostsKey = (currCity, visitedMask)

    if bestCostsKey in bestCosts and bestCosts[bestCostsKey] <= g: # Used to skip paths that have less cost than the bestCosting one already
      continue
    
    bestCosts[bestCostsKey] = g

    for neighbor in range(numCities):
      if visitedMask & (1 << neighbor): # Skips visted cities
        continue

      if board[currCity][neighbor] <= 0: # Skips invalid cities (Ex: ones your currently on)
        continue

      nextMask = visitedMask | (1 << neighbor)
      chosenG = g + board[currCity][neighbor]
      chosenF = chosenG + heuristic(neighbor, nextMask)

      priQueue.append((chosenF, chosenG, neighbor, nextMask, path + [neighbor]))

  return None, None

"""
def generateBoard():
    board=np.zeros((10,10), int)

    for i in range(10):
        for j in range(10-i):
            board[i][j+i] = np.random.randint(1,21)*5

    board = board + np.transpose(board)
    np.fill_diagonal(board, 0)

    '''
    0 x x x x...
    x 0 x x x...
    x x 0 x x...
    x x x 0 x...
    x x x x 0...

    each row i is a location i
    each x in column j is the cost to move from location i to location j

    x is a random multiple of 5 between 5 and 100, symmetrical around the diagonal
    '''

    return board

board = generateBoard()
def printBoard(board):
    print(board)

aStarTsp(board) """
