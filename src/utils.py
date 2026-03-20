import numpy as np

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
    
    x is a random multiple of 5 between 5 and 100
    '''
    
    return board

def printBoard(board):
    print(board)
