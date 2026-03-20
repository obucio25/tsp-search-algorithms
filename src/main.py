import utils
import greedy
import bfs
import dfs

board = utils.generateBoard()
utils.printBoard(board)

greedyCost=greedy.greedy(board)
bfsCost=bfs.bfs(board)
dfsCost=dfs.dfs(board)

print("\nCost to make all sales using:")
print(f'Greedy = {greedyCost}')
print(f'BFS = {bfsCost}')
print(f'DFS = {dfsCost}')

#add whatever other searches u used
