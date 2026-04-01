import numpy as np

def generateBoard(size):
    
    board=np.zeros((size,size), int)
    
    for i in range(size):
        for j in range(size-i):
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
    n = len(board)
    print(board)
    print(f'{n}x{n} board, {n} locations')
