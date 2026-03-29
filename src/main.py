import utils
import greedy
import bfs
import dfs
import aStarTsp #might need .py

board = utils.generateBoard()
utils.printBoard(board)

greedyCost=greedy.greedy(board)
bfsCost=bfs.bfs(board)
dfsCost=dfs.dfs(board)

print("\nCost to make all sales using:")
print(f'Greedy = {greedyCost}')
print(f'BFS = {bfsCost}')
print(f'DFS = {dfsCost}')
print(f'aStarTsp = ')
aStarTsp(board)

#add whatever other searches u used
