import itertools

def route_cost(board, route):
    cost = 0
    for i in range(len(route) - 1):
        cost += board[route[i]][route[i + 1]]
    cost += board[route[-1]][route[0]]
    return cost

def dfs(board):
    numCities = len(board)

    if numCities <= 1:
        return 0, [0]

    bestPath = None
    bestCost = float('inf')

    for perm in itertools.permutations(range(1, numCities)):
        currPath = [0] + list(perm)
        currCost = route_cost(board, currPath)

        if currCost < bestCost:
            bestCost = currCost
            bestPath = currPath[:]

    return bestCost, bestPath + [0]
