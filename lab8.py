import random

def initialize_population(pop_size, string_length):
    population = []
    for _ in range(pop_size):
        individual = ''.join(random.choice('01') for i in range(string_length))  
        population.append(individual)
    return population
def calculate_fitness(individual):
    return individual.count('1')  
def select_parents(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    selection_probs = [f / total_fitness for f in fitness_scores]  
    parent1 = random.choices(population, weights=selection_probs, k=1)[0]
    parent2 = random.choices(population, weights=selection_probs, k=1)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)  
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]  
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]  
    return offspring1, offspring2

def mutate(individual, mutation_rate):
    individual = list(individual)  
    for i in range(len(individual)):
        if random.random() < mutation_rate:  
            individual[i] = '1' if individual[i] == '0' else '0'
    return ''.join(individual)  

def genetic_algorithm(string_length, pop_size, num_generations, mutation_rate):
    population = initialize_population(pop_size, string_length)
    
    for generation in range(num_generations):
        fitness_scores = [calculate_fitness(individual) for individual in population]
        
        best_fitness = max(fitness_scores)
        if best_fitness == string_length: 
            print(f"Optimal solution found in generation {generation}")
            break
        
        next_generation = []
        while len(next_generation) < pop_size:
            parent1, parent2 = select_parents(population, fitness_scores)
            offspring1, offspring2 = crossover(parent1, parent2)
            offspring1 = mutate(offspring1, mutation_rate)
            offspring2 = mutate(offspring2, mutation_rate)
            next_generation.extend([offspring1, offspring2])
        population = next_generation[:pop_size]
        best_individual = population[fitness_scores.index(best_fitness)]
        print(f"Generation {generation}: Best individual: {best_individual} with fitness: {best_fitness}")
    
    fitness_scores = [calculate_fitness(individual) for individual in population]
    best_solution = population[fitness_scores.index(max(fitness_scores))]
    return best_solution

if __name__ == "__main__":
    string_length = 10  
    pop_size = 20 
    num_generations = 100 
    mutation_rate = 0.05  

    best_solution = genetic_algorithm(string_length, pop_size, num_generations, mutation_rate)
    print(f"Best solution: {best_solution} with fitness: {calculate_fitness(best_solution)}")
