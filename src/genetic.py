import random

def route_cost(board, route):
  cost = 0

  for i in range(len(route) - 1):
    cost += board[route[i]][route[i + 1]]

  cost += board[route[-1]][route[0]]
  return cost

def create_route(numCities):
  route = list(range(1, numCities))
  random.shuffle(route)
  return [0] + route

def create_population(popSize, numCities):
  population = []

  for _ in range(popSize):
    population.append(create_route(numCities))

  return population

def fitness(board, route):
  cost = route_cost(board, route)
  return 1 / cost

def roulette_selection(population, fitnesses):
  totalFitness = sum(fitnesses)
  pick = random.uniform(0, totalFitness)

  current = 0
  for i in range(len(population)):
    current += fitnesses[i]
    if current >= pick:
      return population[i]
    
  return population[-1]

def crossover(parent1, parent2):
  size = len(parent1)
  start, end = sorted(random.sample(range(1, size), 2))

  child = [-1] * size
  child[0] = 0

  for i in range(start, end):
    child[i] = parent1[i]

  p2Cities = [city for city in parent2 if city not in child]

  for i in range(1, size):
    if child[i] == -1:
      child[i] = p2Cities.pop(0)

  return child

def mutate(route, mutationRate):
  newRoute = route[:]

  if random.random() < mutationRate:
    i, j = random.sample(range(1, len(newRoute)), 2)
    newRoute[i], newRoute[j] = newRoute[j], newRoute[i]

  return newRoute

def genetic(board, popSize=100, generations=200, mutationRate=0.05):
  numCities = len(board)
  population = create_population(popSize, numCities)

  bestRoute = population[0][:]
  bestCost = route_cost(board, bestRoute)

  for _ in range(generations):
    fitnesses = [fitness(board, route) for route in population]

    for route in population:
      cost = route_cost(board, route)
      if cost < bestCost:
        bestCost = cost
        bestRoute = route[:]

    newPopulation = []

    while len(newPopulation) < popSize:
      parent1 = roulette_selection(population, fitnesses)
      parent2 = roulette_selection(population, fitnesses)

      child = crossover(parent1, parent2)
      child = mutate(child, mutationRate)

      newPopulation.append(child)

    population = newPopulation
  
  return bestRoute + [bestRoute[0]], bestCost