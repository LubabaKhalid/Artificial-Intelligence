import random
import numpy as np


distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

POPULATION_SIZE = 10
NUM_GENERATIONS = 100
MUTATION_RATE = 0.1


def calculate_fitness(route):
    total_distance = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    total_distance += distance_matrix[route[-1]][route[0]]
    return 1 / total_distance  
def initialize_population(num_cities):
    population = []
    for _ in range(POPULATION_SIZE):
        route = list(range(num_cities))
        random.shuffle(route)
        population.append(route)
    return population

def tournament_selection(population, fitness_scores, k=3):
    selected = random.sample(range(len(population)), k)
    selected.sort(key=lambda i: fitness_scores[i], reverse=True)
    return population[selected[0]]

def pmx_crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    
    child[start:end+1] = parent1[start:end+1]

    for i in range(start, end+1):
        if parent2[i] not in child:
            pos = i
            while start <= pos <= end:
                pos = parent2.index(parent1[pos])
            child[pos] = parent2[i]

    for i in range(size):
        if child[i] is None:
            child[i] = parent2[i]

    return child

def mutate(route):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]

def genetic_algorithm(num_cities):
    population = initialize_population(num_cities)
    
    for generation in range(NUM_GENERATIONS):
        fitness_scores = [calculate_fitness(route) for route in population]
        
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1 = tournament_selection(population, fitness_scores)
            parent2 = tournament_selection(population, fitness_scores)
            
            child1 = pmx_crossover(parent1, parent2)
            child2 = pmx_crossover(parent2, parent1)
            
            mutate(child1)
            mutate(child2)
            
            new_population.extend([child1, child2])
        
        population = new_population
    
    best_route = max(population, key=calculate_fitness)
    best_distance = 1 / calculate_fitness(best_route)
    
    return best_route, best_distance

best_route, best_distance = genetic_algorithm(len(distance_matrix))
print("Best Route:", best_route)
print("Best Distance:", best_distance)
