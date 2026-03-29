import utils
import greedy
import genetic
# import bfs
# import dfs

board = utils.generateBoard()
utils.printBoard(board)

greedyCost=greedy.greedy(board)
geneticPath, geneticCost = genetic.genetic(board)
# bfsCost=bfs.bfs(board)
# dfsCost=dfs.dfs(board)

print("\nCost to make all sales using:")
print(f'Greedy = {greedyCost}')
print(f'Genetic = {geneticCost}')

print("\nBest paths:")
print(f"Genetic Path = {geneticPath}")
# print(f'BFS = {bfsCost}')
# print(f'DFS = {dfsCost}')

#add whatever other searches u used
