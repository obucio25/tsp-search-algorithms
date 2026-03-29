import random

# Calculate total cost of a route
def route_cost(board, route):
  cost = 0
  # Sum cost between consecutive cities
  for i in range(len(route) - 1):
    cost += board[route[i]][route[i + 1]]
  
  # Add cost to return to starting city, completing the cycle
  cost += board[route[-1]][route[0]]
  return cost

# Create a single random route
def create_route(numCities):
  # Starts with cities 1 to n-1, excluding zero
  route = list(range(1, numCities))

  # Shuffles cities randomly
  random.shuffle(route)

  # Always start from city 0
  return [0] + route

# Create initial population of routes
def create_population(popSize, numCities):
  population = []

  # Generate popSize number of random routes
  for _ in range(popSize):
    population.append(create_route(numCities))

  return population

# Fitness function, the higher the fitness the better the solution
def fitness(board, route):
  cost = route_cost(board, route)

  # Inverse of cost, since we minimize cost
  return 1 / cost

# Roulette wheel selection, which selects individuals based on fitness prob
def roulette_selection(population, fitnesses):
  # Total fitness of population
  totalFitness = sum(fitnesses)
  # Pick a random value between 0 and total fitness
  pick = random.uniform(0, totalFitness)

  current = 0
  for i in range(len(population)):
    current += fitnesses[i]

    # Return the individual where cumulative fitness exceeds pick
    if current >= pick:
      return population[i]
    
  # Fallback but shouldn't happen if rarely
  return population[-1]

# Crossover, combines two parents into child
def crossover(parent1, parent2):
  size = len(parent1)

  # Pick two crossover points, excluding index 0
  start, end = sorted(random.sample(range(1, size), 2))

  # initialize child with placeholders
  child = [-1] * size
  child[0] = 0 # always start from city 0

  # Copy segment from parent1
  for i in range(start, end):
    child[i] = parent1[i]
  
  # Fill remaining positions using parent2 order
  p2Cities = [city for city in parent2 if city not in child]

  for i in range(1, size):
    if child[i] == -1:
      child[i] = p2Cities.pop(0)

  return child

# Mutation, swaps two cities exluding the start city
def mutate(route, mutationRate):
  newRoute = route[:] # copy route

  # Perform mutation with given probability 
  if random.random() < mutationRate:
    i, j = random.sample(range(1, len(newRoute)), 2)

    # Swap two cities
    newRoute[i], newRoute[j] = newRoute[j], newRoute[i]

  return newRoute

# 2-opt local optimization, improving route by reversing segements
def two_opt(board, route):
  bestRoute = route[:]
  bestCost = route_cost(board, bestRoute)
  improved = True

  # Keep improving until no better solution is found
  while improved:
    improved = False

    # Try all pairs of indices
    for i in range(1, len(bestRoute) - 2):
      for j in range(i + 1, len(bestRoute)):
        
        # Skip adjacent edges, no change
        if j - i == 1:
          continue
        # Create a new route by reversing segment
        newRoute = bestRoute[:]
        newRoute[i:j] = reversed(newRoute[i:j])

        newCost = route_cost(board, newRoute)

        # If improvement found, update best
        if newCost < bestCost:
          bestRoute = newRoute
          bestCost = newCost
          improved = True

    # if improved, loop again and keep trying to improve further

  return bestRoute

# Main genetic algorithm
def genetic(board, popSize=100, generations=200, mutationRate=0.05, eliteCount=3):
  numCities = len(board)

  # Create initial population
  population = create_population(popSize, numCities)

  # Initilize best solution
  bestRoute = population[0][:]
  bestCost = route_cost(board, bestRoute)

  # Evolution loop
  for _ in range(generations):

    # Computes fitness for all individuals
    fitnesses = [fitness(board, route) for route in population]

    # elitism block
    # Sort population by route cost, best first
    sortedPopulation = sorted(population, key=lambda route: route_cost(board, route))

    # Best route of this generation
    generationBest = sortedPopulation[0]
    generationBestCost = route_cost(board, generationBest)
    
    # Update global best if it improves
    if generationBestCost < bestCost:
      bestCost = generationBestCost
      bestRoute = generationBest[:]

    # Top-3 elitism
    newPopulation = [route[:] for route in sortedPopulation[:eliteCount]]

    # Generates rest of new pop 
    while len(newPopulation) < popSize:

      # Select two parents
      parent1 = roulette_selection(population, fitnesses)
      parent2 = roulette_selection(population, fitnesses)
      
      # Ensure parents are not identical, make sure there is diversity
      while parent2 == parent1:
        parent2 = roulette_selection(population, fitnesses)

      # Create child via crossover
      child = crossover(parent1, parent2)

      # Apply mutation
      child = mutate(child, mutationRate)

      # Apply local optimization the 2-opt part
      child = two_opt(board, child)

      # Add child to new population
      newPopulation.append(child)

    # Replace old pop with new population
    population = newPopulation
  
  # returns best route (complete cycle) and best cost
  return bestRoute + [bestRoute[0]], bestCost