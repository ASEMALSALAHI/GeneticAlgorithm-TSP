import random

# Read the file and save the coordinates into a matrix
with open('C:/Users/user1/Desktop/192803004_ASEM_ALSALAHI/tsp_124_1.txt') as f:
    size = int(f.readline())
    coordinates = [list(map(int, line.split())) for line in f]

# Define the genetic algorithm parameters
POPULATION_SIZE = 200
MUTATION_RATE = 0.1
GENERATIONS = 1000

# Define a function to calculate the distance between two cities
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Define the fitness function for the genetic algorithm
def fitness(individual, coordinates):
    total_distance = 0
    for i in range(len(individual)):
        city1 = coordinates[individual[i]]
        city2 = coordinates[individual[(i + 1) % len(individual)]]
        total_distance += distance(city1, city2)
    return 1 / total_distance

# Define the crossover function for the genetic algorithm
def crossover(parent1, parent2):
    child = [-1] * len(parent1)
    start = random.randint(0, len(parent1) - 1)
    end = random.randint(0, len(parent1) - 1)
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        child[i] = parent1[i]
    j = 0
    for i in range(len(parent2)):
        if parent2[i] not in child:
            while child[j] != -1:
                j += 1
            child[j] = parent2[i]
    return child

# Define the mutation function for the genetic algorithm
def mutate(individual):
    i = random.randint(0, len(individual) - 1)
    j = random.randint(0, len(individual) - 1)
    individual[i], individual[j] = individual[j], individual[i]
    return individual

# Initialize the population randomly
population = [list(range(size)) for i in range(POPULATION_SIZE)]
for individual in population:
    random.shuffle(individual)

# Evolve the population using the genetic algorithm
for generation in range(GENERATIONS):
    # Evaluate the fitness of each individual
    fitness_values = [fitness(individual, coordinates) for individual in population]
    # Select the parents for crossover
    parents = random.choices(population, weights=fitness_values, k=POPULATION_SIZE)
    # Create the next generation by crossover and mutation
    next_generation = []
    for i in range(POPULATION_SIZE):
        parent1 = parents[i]
        parent2 = random.choice(parents)
        child = crossover(parent1, parent2)
        if random.random() < MUTATION_RATE:
            child = mutate(child)
        next_generation.append(child)
    population = next_generation

# Find the best individual
best_individual = max(population, key=lambda individual: fitness(individual, coordinates))

# Print the result
print('Optimal maliyet degeri: :', 1 / fitness(best_individual, coordinates))
print('Optimal çözüm için sırası ile gidilecek nodelar (şehirler):', best_individual)