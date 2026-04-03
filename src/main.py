import utils
import greedy
import genetic
import dfs
import aStarTsp

board = utils.generateBoard(10) # 10x10
utils.printBoard(board)

greedyCost, greedyPath = greedy.greedy(board)
geneticPath, geneticCost = genetic.genetic(
    board,
    popSize=200,
    generations=500,
    mutationRate=0.05
)
dfsCost, dfsPath = dfs.dfs(board)

print("\nCost to make all sales using:")
print(f'Greedy = {greedyCost}')
print(f'Genetic = {geneticCost}')
print(f'DFS = {dfsCost}')

print("\nBest paths:")
print(f'Greedy Path = {greedyPath}')
print(f"Genetic Path = {geneticPath}\n")
print(f'DFS Path = {dfsPath}')
print(f'aStarTsp = ')
aStarTsp.aStarTsp(board)

