import random

class World:
    def __init__(self, size):
        self.size = size
        self.grid = self._generate_random_world()

    def _generate_random_world(self):
        return [[random.randint(0, 10) for _ in range(self.size[1])] for _ in range(self.size[0])]

    def fitness(self):
        fitness_score = 0
        for row in self.grid:
            fitness_score += sum(row)
        return fitness_score

    def mutate(self):
        for _ in range(3):  # Más mutaciones para mayor variabilidad
            x = random.randint(0, self.size[0] - 1)
            y = random.randint(0, self.size[1] - 1)
            self.grid[x][y] = random.randint(0, 10)

    @staticmethod
    def crossover(parent1, parent2):
        size = parent1.size
        child_grid = []
        for i in range(size[0]):
            row = []
            for j in range(size[1]):
                if random.random() < 0.5:
                    row.append(parent1.grid[i][j])
                else:
                    row.append(parent2.grid[i][j])
            child_grid.append(row)
        child = World(size)
        child.grid = child_grid
        return child

    def is_similar(self, other, similarity_threshold=0.98):
        size = self.size[0] * self.size[1]
        similar_cells = sum(1 for i in range(self.size[0]) for j in range(self.size[1]) if self.grid[i][j] == other.grid[i][j])
        return (similar_cells / size) >= similarity_threshold

    def difference(self, other):
        size = self.size[0] * self.size[1]
        different_cells = sum(1 for i in range(self.size[0]) for j in range(self.size[1]) if self.grid[i][j] != other.grid[i][j])
        return different_cells / size
