from world import World
from genetic_algorithm import GeneticAlgorithm
from visualizer import Visualizer

# Crear población inicial
population_size = 25
world_size = (10, 10)
initial_population = [World(world_size) for _ in range(population_size)]

# Configurar algoritmo genético
algorithm = GeneticAlgorithm(initial_population)

# Configurar visualizador
visualizer = Visualizer(algorithm)

# Ejecutar ciclo de evolución
while not algorithm.has_converged():
    algorithm.evolve()
    visualizer.update(algorithm.population, algorithm.generation)

# Mostrar visualización final
visualizer.show_final()
