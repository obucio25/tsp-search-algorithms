# tsp-search-algorithms

## Group 1
Implementation and comparison of search algorithms for the Traveling Salesman Problem (TSP) - COSC 4368 AI

---

## Overview
This project explores different approaches to solving the **Traveling Salesman Problem (TSP)**, where the goal is to find the shortest possible route that visits each city exactly once and returns to the starting point.

We implemented and compared multiple algorithms:
- Greedy Search
- A* Search
- Genetic Algorithm (Evolutionary Computing)
- Simulated Annealing

Each algorithm is tested on randomly generated distance matrices.

---

## Algorithms Implemented

### 🔹 Greedy Search (`greedy.py`)
The Greedy algorithm builds a route by always selecting the nearest unvisited city at each step.

- Fast and simple
- Low computational cost
- Does **not guarantee optimal solution**
- Often gets stuck in locally optimal paths

---

### 🔹 A* Search (`aStarTsp.py`)
A* is a heuristic-based search algorithm that explores paths based on both:
- cost so far (g)
- estimated remaining cost (h)

- More informed than Greedy
- Attempts to find optimal or near-optimal solutions
- Computationally expensive as problem size increases

---

### 🔹 Genetic Algorithm (`genetic.py`)
The Genetic Algorithm (GA) uses principles of **evolutionary computing** to iteratively improve solutions.

#### Key Features:
- Population-based search (multiple routes at once)
- Roulette wheel selection (fitness-based)
- Crossover (combines parent routes)
- Mutation (introduces randomness)
- **Elitism (top solutions preserved across generations)**
- **Parent diversity enforcement**
- **2-opt local optimization (route refinement)**

#### How it works:
1. Generate an initial population of random routes
2. Evaluate fitness (inverse of route cost)
3. Select parents probabilistically
4. Create new routes using crossover and mutation
5. Improve routes using 2-opt local search
6. Repeat for multiple generations

#### Performance So Far:
- Consistently outperforms Greedy Search
- Often matches A* solution quality
- More scalable for larger problem sizes

---

### 🔹 Simulated Annealing (`simulatedAnnealing.py`)
Simulated Annealing is a probabilistic local search algorithm inspired by the metallurgical process of slowly cooling heated metal to reduce defects.

#### Key Features:
- Starts from a random tour
- Generates neighbors by swapping two random cities
- Always accepts improvements
- **Accepts worse solutions probabilistically** to escape local optima
- Temperature decreases over time, gradually reducing exploration

#### How it works:
1. Generate a random initial tour
2. Swap two random cities to produce a neighboring tour
3. If the neighbor is better, accept it
4. If the neighbor is worse, accept it with probability e^(-Δ/T)
5. Reduce the temperature each iteration
6. Repeat until temperature falls below the minimum threshold

#### Performance:
- Consistently outperforms Greedy Search
- Competitive with Genetic Algorithm on smaller problem sizes
- Solution quality varies between runs due to random starting tour

---

## How to Run

From the project root:

```bash
python src/main.py