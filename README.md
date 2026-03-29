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

## How to Run

From the project root:

```bash
python src/main.py