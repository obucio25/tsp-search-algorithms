import utils
import greedy
import genetic
import simulatedAnnealing
# import dfs
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
# dfsCost=dfs.dfs(board)
saCost, saPath = simulatedAnnealing.simulatedAnnealing(board)

print("\nCost to make all sales using:")
print(f'Greedy = {greedyCost}')
print(f'Genetic = {geneticCost}')
print(f'Simulated Annealing = {saCost}')

print("\nBest paths:")
print(f'Greedy Path = {greedyPath}')
print(f"Genetic Path = {geneticPath}")
print(f'Simulated Annealing Path = {saPath}')
print(f'aStarTsp = ')
aStarTsp.aStarTsp(board)
# print(f'DFS = {dfsCost}')
