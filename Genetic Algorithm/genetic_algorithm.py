import random
from world import World

class GeneticAlgorithm:
    def __init__(self, population, mutation_rate=0.1, tournament_size=3, diversity_threshold=0.2, similarity_threshold=0.95):
        self.population = population
        self.generation = 0
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size
        self.diversity_threshold = diversity_threshold
        self.similarity_threshold = similarity_threshold

    def select(self):
        tournament = random.sample(self.population, self.tournament_size)
        tournament.sort(key=lambda world: world.fitness(), reverse=True)
        return tournament[0], tournament[1]

    def evolve(self):
        new_population = []
        for _ in range(len(self.population)):
            parent1, parent2 = self.select()
            child = World.crossover(parent1, parent2)
            if random.random() < self.mutation_rate:
                child.mutate()
            new_population.append(child)
        self.population = new_population
        self.generation += 1

    def has_converged(self):
        diversity = self.calculate_diversity()
        if diversity < self.diversity_threshold:
            return True
        
        visual_convergence = self.visual_convergence()
        return visual_convergence

    def calculate_diversity(self):
        total_difference = 0
        num_comparisons = 0
        for i in range(len(self.population)):
            for j in range(i + 1, len(self.population)):
                total_difference += self.population[i].difference(self.population[j])
                num_comparisons += 1
        average_difference = total_difference / num_comparisons if num_comparisons > 0 else 0
        return average_difference
    
    def visual_convergence(self):
        first_world = self.population[0]
        similar_worlds = sum(1 for world in self.population if first_world.is_similar(world, self.similarity_threshold))
        return similar_worlds / len(self.population) >= self.similarity_threshold
