import random

# Initialize the population with random binary strings
def initialize_population(pop_size, string_length):
    population = []
    for _ in range(pop_size):
        individual = ''.join(random.choice('01') for _ in range(string_length))  # Random binary string
        population.append(individual)
    return population

# Calculate fitness for an individual
def calculate_fitness(individual):
    return individual.count('1')  # Fitness is the number of 1s in the string

# Select parents based on fitness (roulette wheel selection or tournament selection)
def select_parents(population, fitness_scores):
    # We can use roulette wheel selection for parent selection
    total_fitness = sum(fitness_scores)
    selection_probs = [f / total_fitness for f in fitness_scores]  # Normalize fitness to create probabilities
    parent1 = random.choices(population, weights=selection_probs, k=1)[0]
    parent2 = random.choices(population, weights=selection_probs, k=1)[0]
    return parent1, parent2

# Perform crossover to generate offspring
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)  # Random point for crossover
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]  # Combine parts
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]  # Swap parts for second offspring
    return offspring1, offspring2

# Apply mutation to introduce diversity
def mutate(individual, mutation_rate):
    individual = list(individual)  # Convert to list to mutate easily
    for i in range(len(individual)):
        if random.random() < mutation_rate:  # Flip bit with mutation probability
            individual[i] = '1' if individual[i] == '0' else '0'
    return ''.join(individual)  # Convert back to string

# Genetic Algorithm implementation
def genetic_algorithm(string_length, pop_size, num_generations, mutation_rate):
    # Step 1: Initialize population
    population = initialize_population(pop_size, string_length)
    
    # Repeat for a fixed number of generations
    for generation in range(num_generations):
        # Step 2: Calculate fitness for the current population
        fitness_scores = [calculate_fitness(individual) for individual in population]
        
        # Step 3: Check for the best solution (stop if perfect solution is found)
        best_fitness = max(fitness_scores)
        if best_fitness == string_length:  # If all ones are found, stop early
            print(f"Optimal solution found in generation {generation}")
            break
        
        # Step 4: Create the next generation through selection, crossover, and mutation
        next_generation = []
        while len(next_generation) < pop_size:
            # Select parents
            parent1, parent2 = select_parents(population, fitness_scores)
            
            # Perform crossover to create offspring
            offspring1, offspring2 = crossover(parent1, parent2)
            
            # Apply mutation to both offspring
            offspring1 = mutate(offspring1, mutation_rate)
            offspring2 = mutate(offspring2, mutation_rate)
            
            # Add the offspring to the next generation
            next_generation.extend([offspring1, offspring2])
        
        # Keep the population size fixed
        population = next_generation[:pop_size]
        
        # Output the best solution of this generation
        best_individual = population[fitness_scores.index(best_fitness)]
        print(f"Generation {generation}: Best individual: {best_individual} with fitness: {best_fitness}")
    
    # Return the best solution from the final generation
    fitness_scores = [calculate_fitness(individual) for individual in population]
    best_solution = population[fitness_scores.index(max(fitness_scores))]
    return best_solution

# Example of running the genetic algorithm
if __name__ == "__main__":
    # Set parameters
    string_length = 10  # Length of the binary string
    pop_size = 20  # Population size
    num_generations = 100  # Number of generations
    mutation_rate = 0.05  # Mutation rate

    # Run the genetic algorithm
    best_solution = genetic_algorithm(string_length, pop_size, num_generations, mutation_rate)
    print(f"Best solution: {best_solution} with fitness: {calculate_fitness(best_solution)}")
